#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
form=cgi.FieldStorage()
uname=form.getvalue("uname")
upwd=form.getvalue("upwd")
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    if uname=='Admin' and upwd=='Admin':
        try:
            insertQuery="insert into tbl_admin_session values('%s','%s')"%(uname,upwd)
            cursor.execute(insertQuery)
            db.commit()
            print "<script>alert('Login Success');location.href='adminhomepage.py';</script>"
        except:
            db.rollback()
            print "<script>alert('Invalid Credentials');location.href='index.py';</script>"
    else:
        selectQuery="select * from tb1_register where upassword='%s' and username='%s' or emailid='%s'"%(upwd,uname,uname)
        if cursor.execute(selectQuery)>0:
            try:
                result=cursor.fetchone()
                sessid=result[0]
                insertQuery="insert into tbl_user_session values(%d,'%s','%s')"%(int(sessid),uname,upwd)
                cursor.execute(insertQuery)
                db.commit()
                print "<script>alert('Login Success');location.href='userhomepage.py?sid=%s';</script>"%(sessid)
            except:
                db.rollback()
                print "<script>alert('Invalid Credentials');location.href='index.py';</script>"            
            #print "<script>alert('Login Success');location.href='userhomepage.py';</script>"
        else:
            print "<script>alert('Invalid Credentials');location.href='index.py';</script>"
else:
    print "Error in Connecting with Server"
    
