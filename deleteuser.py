#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
form=cgi.FieldStorage()
userid=form.getvalue("uid")
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    try:
        
        deleteQuery="delete from tb1_register where userid=%d"%(int(userid))
        cursor.execute(deleteQuery)
        db.commit()
        print "<script>alert('Deleted Successfully');location.href='adminhomepage.py';</script>"
    except:
        db.rollback()
        print "<script>alert('Error in Deletion');location.href='adminhomepage.py';</script>"
else:
    print "Error in Connecting With Server"
    
