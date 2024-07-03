from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return
        
        if self.path == "/data":

            data = {"name": "John", "age": 30, "city": "New York"}

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            json_data = json.dumps(data)
            encoded_data = json_data.encode()
            self.wfile.write(encoded_data)
            return 
        
        if self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
            return
        
        if self.path == "/info":
            info_data = {"version": "1.0", "description": "A simple API built with http.server"}
            info_string = json.dumps(info_data)
            encoded_data = info_string.encode()

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(encoded_data)  

        self.send_response(404)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"404 Not Found")

def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
