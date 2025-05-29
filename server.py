import http.server
import socketserver
import os

PORT = 8000

# 현재 디렉토리를 기준으로 HTML 서빙
web_dir = os.path.join(os.path.dirname(__file__))
os.chdir(web_dir)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"서버 실행 중: http://localhost:{PORT}")
    print("모바일에서도 접속하려면: http://<PC IP>:8000 로 접속")
    httpd.serve_forever()
