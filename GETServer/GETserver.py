from http.server import BaseHTTPRequestHandler, HTTPServer

host = "localhost"
port = 8000
file_path = "hello.txt"


class SimpleHTTPGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/" + file_path

        try:
            with open(self.path[1:], "rb") as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"File not found.")


server_address = (host, port)
httpd = HTTPServer(server_address, SimpleHTTPGetHandler)

print(f"Serving on http://{host}:{port}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print("Server stopped.")
