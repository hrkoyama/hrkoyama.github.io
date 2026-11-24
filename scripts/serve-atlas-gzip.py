#!/usr/bin/env python3
"""Loopback-only gzip fixture for cold-browser measurements, not a deployment server."""
import argparse,gzip,http.server,io,mimetypes,pathlib,urllib.parse

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--port',type=int,default=4198);p.add_argument('--root',type=pathlib.Path,default=pathlib.Path.cwd());a=p.parse_args()
    root=a.root.resolve();compressed={}
    text={'.html','.css','.js','.mjs','.json','.svg','.txt','.md'}
    def encoded(path):
        if path not in compressed:compressed[path]=gzip.compress(path.read_bytes(),compresslevel=9,mtime=0)
        return compressed[path]
    # Warm the server's compression cache, while each browser context stays cold.
    for name in ['search/index.html','numerical-methods-atlas/index.html','search/atlas-query-index.json','search/query-index.json','numerical-methods-atlas/content.en.json','numerical-methods-atlas/content.ja.json']:
        encoded(root/name)
    class Handler(http.server.SimpleHTTPRequestHandler):
        def send_head(self):
            raw=urllib.parse.unquote(urllib.parse.urlsplit(self.path).path)
            path=(root/raw.lstrip('/')).resolve()
            if not path.is_relative_to(root) or any(x.startswith('.') for x in pathlib.PurePosixPath(raw).parts if x!='/'):
                self.send_error(404);return None
            if path.is_dir():path=path/'index.html'
            if not path.is_file():self.send_error(404);return None
            use_gzip=path.suffix in text and 'gzip' in self.headers.get('Accept-Encoding','')
            body=encoded(path) if use_gzip else path.read_bytes()
            self.send_response(200);self.send_header('Content-Type',mimetypes.guess_type(path)[0] or 'application/octet-stream')
            self.send_header('Content-Length',str(len(body)));self.send_header('Cache-Control','no-cache');self.send_header('Vary','Accept-Encoding')
            if use_gzip:self.send_header('Content-Encoding','gzip')
            self.end_headers();return io.BytesIO(body)
    server=http.server.ThreadingHTTPServer(('127.0.0.1',a.port),Handler)
    print(f'Local: http://127.0.0.1:{a.port}/ (gzip fixture)',flush=True)
    try:server.serve_forever()
    finally:server.server_close()

if __name__=='__main__':main()
