#!C:\Users\Akshaylal\AppData\Local\Programs\Python\Python310\python.exe

print('content-type: text/html')

import cgitb
cgitb.enable()

import cgi
import html
import os   # for file upload

try:
    import msvcrt
    # set mode for stdin and stdout
    msvcrt.setmode(0, os.O_BINARY) # stdin = 0
    msvcrt.setmode(1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

firstName = html.escape(form.getvalue('first_name', 'noname'))
lastName = html.escape(form.getvalue('last_name', 'noname'))
vehicle = form.getlist('vehicle')
gender = form.getvalue('gender')
about = html.escape(form.getvalue('about'))

# get the file from the nested Field storage
fileitem = form['file']

# checking if a valid file was loaded
if fileitem.filename:
    # get rid of the path and keep only the filename
    imagename = os.path.basename(fileitem.filename)
    open('files/' + imagename, 'wb').write(fileitem.file.read())
    message = 'The file was uploaded to files/' + imagename
else:
    message = 'No file was uploaded'


print(f'''
<html>
<head>
    <title>Form submit</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="myheadstyle">
        <h1>Hello, { firstName } { lastName }</h1>
        <p>Vehicles: { ", ".join([html.escape(i) for i in vehicle]) }</p>
        <p>Gender: { gender }</p>
        <p>About: { about }</p>
        { fileitem.filename }
        <img src="files/{imagename}">
    </div>
</body>
</html>
''')