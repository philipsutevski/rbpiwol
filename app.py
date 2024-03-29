from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from wakeonlan import send_magic_packet
import logging

class WoLRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as file:
                self.wfile.write(file.read())

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)
            mac_address = params['mac_address'][0]
            send_magic_packet(mac_address)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Wake-on-LAN packet sent to {}'.format(mac_address), 'utf-8'))
        except Exception as e:
            logging.error('Error in do_POST: %s', str(e))
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Error: {}'.format(str(e)), 'utf-8'))

if __name__ == '__main__':
    # Configuring logging
    logging.basicConfig(level=logging.DEBUG)

    # Starting the server
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, WoLRequestHandler)
    logging.info('Starting WoL server on port 5000...')
    httpd.serve_forever()