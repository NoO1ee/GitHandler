from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/webhook":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Webhook received. Pulling...")

            repo_path = r"C:\\Users\\Administrator\\Desktop"
            print(f"Received webhook. Pulling repo at: {repo_path}")

            try:
                result = subprocess.run(
                    ["git", "-C", repo_path, "pull"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    shell=True 
                )
                print("STDOUT:\n", result.stdout)
                print("STDERR:\n", result.stderr)

            except Exception as e:
                print(f"Error pulling repo: {e}")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, WebhookHandler)
    print(f"{bcolors.OKGREEN}🚀 Webhook server running on port 8080...{bcolors.ENDC}")
    httpd.serve_forever()