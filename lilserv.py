import http.server
import socketserver
import sys

if (len(sys.argv) != 2):
	print("Usage: python3 server.py file.sh 1337")

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Define shell file
        self.path = sys.argv[1]
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Define usage local port
PORT = int(sys.argv[2])

my_handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), my_handler) as httpd:
    print("Listening on port: ", PORT)
    httpd.serve_forever()
