import os
import socket
import http.server
import socketserver
import sys

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def main():
    directory = "c:/Users/lyies/Desktop/siteelk/localhost_v2"
    port = find_free_port()
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

    print(f"==================================================")
    print(f"Server starting for {directory}")
    print(f"URL: http://localhost:{port}")
    print(f"==================================================")
    sys.stdout.flush()

    with socketserver.TCPServer(("", port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

if __name__ == "__main__":
    main()
