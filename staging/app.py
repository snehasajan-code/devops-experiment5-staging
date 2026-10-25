from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.environ.get("APP_MESSAGE", "Hello from Docker Compose!")
        hostname = socket.gethostname()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        self.wfile.write(f"""
        <html>
          <head><title>DevOps Experiment 4</title></head>
          <body style="font-family: Arial; text-align: center; margin-top: 80px;">
            <h1>{message}</h1>
            <p>Container hostname: {hostname}</p>
            <p>Infrastructure as Code with Docker Compose</p>
          </body>
        </html>
        """.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("App listening on port 8000", flush=True)
server.serve_forever()
