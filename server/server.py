"""Server for the project."""

# Python
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# Urls
from properties import url_resolver


class MyHandler(BaseHTTPRequestHandler):
    """Class for handling requests.

    MyHandler is a subclass of BaseHTTPRequestHandler
    allowing http requests that arrive at the server.
    """

    def do_HEAD(self):
        """Handle HEAD requests."""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        """Handle GET requests."""
        parsed_path = urlparse(self.path).path
        query = urlparse(self.path).query
        query_params = parse_qs(query)
        status_code, response = url_resolver(
            path=parsed_path,
            request_type=self.command,
            query_params=query_params
        )
        self.respond(status_code, response)

    def respond(self, status_code, data):
        """Send response to client."""
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        content = bytes(json.dumps(data), 'utf-8')
        self.wfile.write(content)
