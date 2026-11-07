
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        version = os.getenv("APP_VERSION", "1.0.0")

        if self.path == "/test":
            message = "CloudDeploy service is running"
        elif self.path == "/version":
            message = f"Version: {version}"
        else:
            self.send_error(404, "Not Found")
            return

        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode())


server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Service running on port 8080", flush=True)
server.serve_forever()
