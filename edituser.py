#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
import MySQLdb
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    selectQuery="select * from tbl_user_session"
    if cursor.execute(selectQuery)==0:
        print "<script>alert('session is expired');location.href='index.py';</script>"
    else:
        print "<html><head>"
        print "<link rel='stylesheet' type='text/css' href='style.css'>"
        print "<script src='validation.js'></script>"
        print "</head>"
        print "<body onLoad='onCountry()'>"
        print "<form name='usereditpage' action='updateuser.py' method='post' enctype='multipart/form-data'>"
        import edituser_layout		
        print "</form></body></html>"
else:
    print "Error in Connecting with Server"
