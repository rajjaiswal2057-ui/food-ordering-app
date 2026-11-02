import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from menu import get_menu

PORT = 5000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/menu":
            body, status = json.dumps(get_menu()), 200
        elif self.path == "/":
            body, status = json.dumps({"app": "Online Food Ordering", "status": "running"}), 200
        else:
            body, status = json.dumps({"error": "not found"}), 404
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    print(f"Food ordering app listening on port {PORT}", flush=True)
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
