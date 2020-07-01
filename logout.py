#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    try:
        
        deleteQuery="delete from tbl_admin_session"
        cursor.execute(deleteQuery)
        db.commit()
        print "<script>location.href='index.py';</script>"
    except:
        db.rollback()
else:
    print "Error in Connecting with Server"
