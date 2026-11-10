#!/usr/bin/env python3
"""Serve the Bigme HiBreak Pro simulator locally."""

from __future__ import annotations

import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def main() -> None:
    port = int(os.environ.get("PORT", "8000"))
    directory = os.getcwd()

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    httpd = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    print(f"Serving {directory} on http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
