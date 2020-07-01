#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
import MySQLdb
import cgi
form=cgi.FieldStorage()
sessid=form.getvalue("sid")

db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    try:
        
        deleteQuery="delete from tbl_user_session where userid=%d"%(int(sessid))
        cursor.execute(deleteQuery)
        db.commit()
        print "<script>location.href='index.py';</script>"
    except:
        db.rollback()
else:
    print "Error in Connecting with Server"
