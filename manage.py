"""Manage for the project."""

# Http server
from http.server import HTTPServer

# Server
from server.server import MyHandler

PORT = 8000

if __name__ == '__main__':
    httpd = HTTPServer(('', PORT), MyHandler)
    print('Starting server on port: ', PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('Server stopped')
