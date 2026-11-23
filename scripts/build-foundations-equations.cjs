// Authoring-only: MathJax 3.2.2 (npm mathjax-full@3.2.2). Run from repository root.
// Install in a separate directory and expose its node_modules with NODE_PATH.
const fs=require('fs'),path=require('path');
const {mathjax}=require('mathjax-full/js/mathjax.js');const {TeX}=require('mathjax-full/js/input/tex.js');const {SVG}=require('mathjax-full/js/output/svg.js');const {liteAdaptor}=require('mathjax-full/js/adaptors/liteAdaptor.js');const {RegisterHTMLHandler}=require('mathjax-full/js/handlers/html.js');const {AllPackages}=require('mathjax-full/js/input/tex/AllPackages.js');
const adaptor=liteAdaptor();RegisterHTMLHandler(adaptor);const doc=mathjax.document('',{InputJax:new TeX({packages:AllPackages}),OutputJax:new SVG({fontCache:'local'})});
if(require('mathjax-full/package.json').version!=='3.2.2') throw Error('Pinned MathJax 3.2.2 required');
const root=process.cwd(),d=JSON.parse(fs.readFileSync('catalog/atlas-foundations-course.json'));const out=path.join(root,d.base.replace(/^\//,''),d.edition,'equations');fs.mkdirSync(out,{recursive:true});const index={};
for(const c of d.chapters){let i=0;for(const s of c.sections)for(const e of s.equations){i++;let svg=adaptor.innerHTML(doc.convert(e.tex,{display:true}));if(svg.includes('data-mjx-error'))throw Error(e.tex);svg=svg.replace(/width="([\d.]+)ex"/,(_,v)=>`width="${(+v*5.5).toFixed(3)}pt"`).replace(/height="([\d.]+)ex"/,(_,v)=>`height="${(+v*5.5).toFixed(3)}pt"`).replace(/currentColor/g,'#14343b');const file=`equation-${c.id}-${i}.svg`;fs.writeFileSync(path.join(out,file),svg+'\n');index[c.id+'-'+i]={file,tex:e.tex,plain:e.plain};}}
fs.writeFileSync(path.join(out,'index.json'),JSON.stringify(index,null,2)+'\n');console.log(Object.keys(index).length+' equations rendered');
