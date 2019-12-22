#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from time import sleep


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        sleep(10)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


def Listen():
    httpd = ThreadingHTTPServer(('localhost', 8000), HTTPRequestHandler)
    httpd.serve_forever()
