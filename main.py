import json
from io import BytesIO

import guest.main
import http.server
import time
import os


class Server(http.server.BaseHTTPRequestHandler):
    
    def do_POST(self):
        if self.headers['Content-Type'].lower() != "application/json":
            print(f"invalid content type {self.headers['Content-Type']}")
            self.send_response(400)
            self.end_headers()
            return

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        request = json.loads(body)
        try:
            guest_resp = guest.main.skyhook(request, None)
        except Exception as e:
            print("Execution failed:", e)
            time.sleep(5)
            self.send_response(500)
            self.end_headers()
            return

        self.send_response(200)
        self.end_headers()
        # TODO: string intermediary is inefficient
        resp_json = json.dumps(guest_resp)
        self.wfile.write(str.encode(resp_json, 'utf-8'))
        return


def main():
    port = int(os.environ['SKYHOOK_PORT'])

    print("Hello from baseimage")
    server = http.server.HTTPServer(('0.0.0.0', port), Server)
    server.serve_forever()


if __name__ == "__main__":
    main()
