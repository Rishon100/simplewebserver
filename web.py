from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    
        
     <body>
     <h1 align="center">V Rishon Anand (24900460) </h1>
          <pre> <ul type="none">
              <li><b> Device name </b>    DESKTOP-MOHHBTU </li>   
              <li><b> processor </b>      13th Gen Intel(R) Core(TM) i5-1335U 1.30GHz</li>
              <li><b> Installed RAM </b>  16.0 GB (15.7 GB usable) </li>
              <li><b> Device ID </b>      15EEA3B2-7EF5-4DEC-903D-577382C3C005 </li>
              <li><b> Product ID</b>      00342-42709-15891-AAOEM</li>
              <li><b>system type </b>     64-bit operating system, x64-based processor</li>

          </ul></pre>
     </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()