# serve the function locally for testing, without a webframework
if __name__ == '__main__':
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from handler import handle

    class RequestHandler(BaseHTTPRequestHandler):
        def do_POST(self):
            result = handle({
                'body': self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
            })
            self.send_response(result['statusCode'])
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(result['body'].encode('utf-8'))

        def do_OPTIONS(self):
            self.send_response(204)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()

    print("Starting server at http://localhost:8000")
    HTTPServer(("0.0.0.0", 8000), RequestHandler).serve_forever()
