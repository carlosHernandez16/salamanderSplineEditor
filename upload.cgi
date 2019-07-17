# This is the upload script for taking the chosen image and storing it on the server

#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable(display=1, logdir="/Library/WebServer/CGI-Executables/OUTDIR")

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:

    # strip leading path from file name
    # to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    open('../Documents/files/' + fn, 'wb').write(fileitem.file.read())
    message = "File: /files/" + fileitem.filename + ", was uploaded successfully! This tab may be closed."

else:
    message = 'No file was uploaded'

print """\
Content-Type: text/plain\n
%s
""" % (message)
