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
          <pre> <ul type="none">
              <li><b> Device name </b>    DESKTOP-MOHHBTU </li>   
              <li><b> processor </b>      13th Gen Intel(R) Core(TM) i5-1335U 1.30GHz</li>
              <li><b> Installed RAM </b>  yafyuwfuhawouhfohu </li>
              <li><b> Device ID </b>      uabwefouneawofnaouwn </li>
              <li><b> Product ID</b>      awyufwaeiufuwafiujwaiufhia</li>
              <li><b>system type </b>     afnwafeuhwauhfuhwaih</li>

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
![alt text](<Screenshot 2024-11-12 092231.png>)
![alt text](<Screenshot 2024-11-12 092738.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
