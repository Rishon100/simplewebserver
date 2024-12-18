# EX01 Developing a Simple Webserver
## Date:10/10/2024

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
     <body>
     <h1 align="center">V Rishon Anand (24900460) </h1
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
```
## OUTPUT:
![alt text](<Screenshot 2024-11-16 145810-1.png>) 
![alt text](<Screenshot 2024-11-16 145922.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
