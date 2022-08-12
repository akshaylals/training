#!C:\Users\Akshaylal\AppData\Local\Programs\Python\Python310\python.exe

print('content-type: text/html\n\n')

# including cgi traceback manager to get the runtime error data
import cgitb

cgitb.enable()

import sys
sys.stderr = sys.stdout

print(1/0)

print('''
<html>
<head>
    <title>Test Title</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="myheadstyle">
        <h1>My heading</h1>
        <p>My contents</p>
    </div>
</body>
</html>
''')
