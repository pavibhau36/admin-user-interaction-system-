import MySQLdb
import cgi
form=cgi.FieldStorage()
sessid=form.getvalue("sid")
print "<div id='container'>"
print "<div id='header'>"
print "<br>"
print "<center><font color=white><h1>USER DETAILS</h1></font></center>"
print "</div>"
print "<div id='menubar'>"
print "<table width='100%' border=0 id=menutable><tr><td align=center><a href='index.py'>Home</a></td>"
print "<td align=center><a href='adminhomepage.py' active>User Details</a></td>"
print "<td align=center><a href='galler.py'>Gallery</a></td>"
print "<td align=center><a href='contactus.py'>Contact Us</a></td>"
print "<td align=center><a href='userlogout.py?sid=%s'>Logout</a></td>"%(sessid)
print "</tr>"
print "</table>"
print "</div>"
print "<div id='commonpane'>"
print "<br><br>"
print "<table width='80%' id=tableuser align=center border=0 celpadding=0 cellspacing=0>"
print "<tr><th align=center colspan=6>My Details</th></tr>"
print "<tr><th align=center>UserId</th><th align=center>User Name</th>"
print "<th align=center>Mobile</th>"
print "<th align=center>Emailid</th>"
print "<th align=center>Image</th>"
print "<th align=center>Edit</th>"
print "</tr>"
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    
    cursor=db.cursor()
    selectQuery="select userid,username,mobile,emailid,imgname from tb1_register where userid=%d"%(int(sessid))
    
    if cursor.execute(selectQuery)>0:
        results=cursor.fetchall()
        for row in results:
            uid=row[0]
            uname=row[1]
            umobile=row[2]
            uemail=row[3]
            imgname=row[4]
            print "<tr><td align=center>%s</td><td align=center>%s</td><td align=center>%s</td><td align=center>%s</td><td><img src='files/%s' width=50 height=50></td><td align=center><a href='edituser.py?uid=%s'>Edit</a></td></tr>"%(uid,uname,umobile,uemail,imgname,uid)
    else:
        print "<tr><td colspan=5>No Records Available</td></tr>"
else:
    print "Error in Connecting with Server"                                          
print "</table>"
print "</div>"
print "<div id='footer'>"
print "<br>"
print "<center> <font color=white>&copy;Reserved to Company</font></center>"
print "</div>"
print "</div>"
                                  
