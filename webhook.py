from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        subprocess.run(["/var/www/mywebsite/deploy.sh"])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Deployment successful")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 9000)
    httpd = HTTPServer(server_address, WebhookHandler)
    print("Listening for GitHub webhooks on port 9000...")
    httpd.serve_forever()

