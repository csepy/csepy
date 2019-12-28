#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from io import BytesIO
import urllib.parse as urlparse
from urllib.parse import parse_qs
import itertools


serverContext = None


class ServerService:
    def __init__(self, context, host, port):
        global serverContext
        serverContext = context
        self.host = host
        self.port = port

    def Run(self, sysargs):
        RunServer(self.host, self.port)


class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
        function = parsed.path.replace('/','')
        params = ' '.join(list(itertools.chain.from_iterable(parse_qs(parsed.query).values())))
        print(params)
        request = f"{function} {params}"
        global serverContext
        serverContext.CommandQueue.EnqueueCommands([request])
        serverContext.CommandQueue.RunCommands()

        self.Reply(200, f"HelloWorld get: {self.path}")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        parsed = urlparse.urlparse(self.path)
        function = parsed.path.replace('/','')
        params = ' '.join(parse_qs(parsed.query).values())
        print(params)
        request = f"{function} {params}"
        global serverContext
        serverContext.CommandQueue.EnqueueCommands([request])
        serverContext.CommandQueue.RunCommands()

        self.Reply(200, f"HelloWorld post: {self.path} + {body}")

    def Reply(self, errorCode, message):
        bMessage = bytearray()
        bMessage.extend(map(ord, message))
        self.send_response(errorCode)
        self.end_headers()
        response = BytesIO()
        response.write(bMessage)
        self.wfile.write(response.getvalue())


def RunServer(host, port):
    print(f"Listening on {host}:{port}")
    httpd = ThreadingHTTPServer((host, port), HTTPRequestHandler)
    httpd.serve_forever()
