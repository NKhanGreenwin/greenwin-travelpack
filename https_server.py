#!/usr/bin/env python3
import http.server
import ssl
import socketserver
import os

# Change to the directory containing the HTML file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8443

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    # Create SSL context
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    
    # Wrap the socket with SSL
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print(f"🔒 HTTPS Server running at: https://localhost:{PORT}")
    print("📝 TravelPack Portal now secure - autofill should work!")
    print("🔍 Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        httpd.shutdown() 