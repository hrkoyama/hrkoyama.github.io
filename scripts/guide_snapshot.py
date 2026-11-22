"""Keep a local knowledge-pack capture stable until its actual inputs change."""


def capture_stamp(previous, pages, records, now):
    if (previous and previous.get('pages') == pages and previous.get('records') == records
            and isinstance(previous.get('capturedAt'), str) and previous['capturedAt']):
        return previous['capturedAt']
    return now
