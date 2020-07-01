#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
print "<html><head>"
print "<link rel='stylesheet' type='text/css' href='style.css'>"
print "<script src='validation.js'></script>"
print "</head>"
print "<body onLoad='onCountry();'><form name='register' action='registeruser.py' method='post' enctype='multipart/form-data'>"
import signup_layout		
print "</form></body></html>"
