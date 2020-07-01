#!C:\Python27/python.exe
print "content-type:text/html\n\n"
import MySQLdb
import cgi
import smtplib
form=cgi.FieldStorage()
receivers=form.getvalue('uemail')
sender ='pavithra.3698@gmail.com'
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    selectQuery="select upassword from tb1_register where emailid='%s'"%(receivers)
    cursor.execute(selectQuery)
    result=cursor.fetchone()
    yourpwd=result[0]
    message = "From: %s\r\n"%sender+"To: %s\r\n"%receivers+"Subject:%s\r\n"%('Recover Password')+"\r\n"+yourpwd
    try:
        smtpserver=smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(sender,'8807223890')
        smtpserver.sendmail(sender,receivers,message)
        print "<script>alert('Successfully sent email');location.href='forgot.py';</script>"
    except:
        print "<script>alert('Unable to send Email');location.href='forgot.py';</script>"
else:
    print "Error in connecting with server"
