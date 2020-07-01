#!C:\Python27/python.exe
print "Content-Type:text/html\n\n"
import os
import cgi
import MySQLdb
try:
    import msvcrt
    msvcrt.setmode(0,os.O_BINARY)
    msvcrt.setmode(1,os.O_BINARY)
except ImportError:
    pass
form=cgi.FieldStorage()
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
utoc=form.getvalue("utoc")
udob=udate+"-"+umonth+"-"+uyear
fp=form['ufile']
if fp.filename:
    fn=os.path.basename(fp.filename)
    open("files/"+fn,'wb').write(fp.file.read())
    file_name=fn
    print "%s Uploaded Successfully" %(file_name)
else:
    print "no files exist"
    
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    selectQuery="select * from tb1_register where username='%s' and mobile=%d and emailid='%s'"%(uname,int(umobile),uemail)
    print selectQuery
    if cursor.execute(selectQuery)>0:
        print "<script>alert('Already Exists');location.href='signup.py';</script>"
    else:
        try:
            insertQuery="""insert into tb1_register(
            username,firstname,lastname,upassword,mobile,emailid,country,state,city,udob,address,gender,toc,imgname) values('%s','%s','%s','%s',%d,'%s','%s','%s',
            '%s','%s','%s','%s','%s','%s')"""%(uname,fname,lname,upwd,int(umobile),uemail,ucountry,ustate,ucity,udob,uaddress,ugender,utoc,file_name)
            print insertQuery
            cursor.execute(insertQuery)
            db.commit()
            print "<script>alert('Registered Successfully');location.href='index.py';</script>"
        except:
            db.rollback()
            print "<script>alert('Error in Registering');location.href='signup.py';</script>"
            
else:
    print "Error in Connectiong With Server"



