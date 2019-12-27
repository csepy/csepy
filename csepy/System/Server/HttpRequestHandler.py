#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
from time import sleep
import array


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.Reply(200, f"HelloWorld get: {self.path}")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        self.Reply(200, f"HelloWorld post: {self.path} + {body}")

    def Reply(self, errorCode, message):
        bMessage = bytearray()
        bMessage.extend(map(ord, message))
        self.send_response(errorCode)
        self.end_headers()
        response = BytesIO()
        response.write(bMessage)
        self.wfile.write(response.getvalue())


def Listen():
    httpd = ThreadingHTTPServer(('localhost', 8000), HTTPRequestHandler)
    httpd.serve_forever()
