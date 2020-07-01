#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
import cgi
import MySQLdb
form=cgi.FieldStorage()
userid=form.getvalue("userid")
uname=form.getvalue("uname")
fname=form.getvalue("fname")
lname=form.getvalue("lname")
upwd=form.getvalue("upwd")
umobile=form.getvalue("umobile")
uemail=form.getvalue("uemail")
ucountry=form.getvalue("ucountry")
ustate=form.getvalue("ustate")
ucity=form.getvalue("ucity")
udate=form.getvalue("udate")
umonth=form.getvalue("umonth")
uyear=form.getvalue("uyear")
uaddress=form.getvalue("uaddress")
ugender=form.getvalue("ugender")

udob=udate+"-"+umonth+"-"+uyear
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    try:
        updateQuery="""update tb1_register set
            username='%s',firstname='%s',lastname='%s',
            upassword='%s',mobile=%d,emailid='%s',
            country='%s',state='%s',city='%s',udob='%s',
            address='%s',gender='%s' where userid=%d"""%(uname,fname,lname,upwd,int(umobile),uemail,ucountry,ustate,ucity,udob,uaddress,ugender,int(userid))
        cursor.execute(updateQuery)
        db.commit()
        print "<script>alert('Updated Successfully');location.href='userhomepage.py?sid=%s';</script>"%(userid)
    except:
        db.rollback()
        print "<script>alert('Error in Updating');location.href='userhomepage.py';</script>"
            
else:
    print "Error in Connectiong With Server"



