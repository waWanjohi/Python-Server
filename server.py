from http.server import HTTPServer, BaseHTTPRequestHandler

class ServeHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type', 'text/html')
		self.end_headers()
		self.wfile.write('Server is working fine! Path = '.encode())
		self.wfile.write(self.path.encode())




def main():
	httpserver = HTTPServer(('localhost', 8000), ServeHandler)
	print('Server running on http://localhost:8000')
	httpserver.serve_forever()

if __name__ == '__main__':
	main()
