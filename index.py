from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from justwatch import JustWatch
import json

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        qs = parse_qs(urlparse(self.path).query)
        country = qs["country"]
        if country and len(country[0]) > 1:
            justwatch_country = country[0]
        else:
            justwatch_country = 'US'
        just_watch = JustWatch(country=justwatch_country)
        results = just_watch.search_for_item(providers=['mbi'])
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(results).encode())
        return
