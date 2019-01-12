from http.server import BaseHTTPRequestHandler, HTTPServer
from justwatch import JustWatch
import json

just_watch= JustWatch(country='US')

results = just_watch.search_for_item(providers=['mbi'])

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(json.dumps(results)).encode())
        return
