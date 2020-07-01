import MySQLdb
print "<div id='container'>"
print "<div id='header'>"
print "<br>"
print "<center><font color=white><h1>USER HISTORY</h1></font></center>"
print "</div>"
print "<div id='menubar'>"
print "<table width='100%'height='60%' border=0 id=menutable><tr><td align=center><a href='index.py'>Home</a></td>"
print "<td align=center><a href='adminhomepage.py' active>User Details</a></td>"
print "<td align=center><a href='galler.py'>Gallery</a></td>"
print "<td align=center><a href='contactus.py'>Contact Us</a></td>"
print "<td align=center><a href='logout.py'>Logout</a></td>"
print "</tr>"
print "</table>"
print "</div>"
print "<div id='commonpane'>"
print "<br><br>"
print "<table width='80%' height='50%' id=tableuser align=center border=0 celpadding=0 cellspacing=0>"
print "<tr><th align=center colspan=5>User Details</th></tr>"
print "<tr><th align=center>UserId</th><th align=center>User Name</th>"
print "<th align=center>Mobile</th>"
print "<th align=center>Emailid</th>"
print "<th align=center>Delete</th>"
print "</tr>"
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    selectQuery="select userid,username,mobile,emailid from tb1_register"
    if cursor.execute(selectQuery)>0:
        results=cursor.fetchall()
        for row in results:
            uid=row[0]
            uname=row[1]
            umobile=row[2]
            uemail=row[3]
            print "<tr><td align=center>%s</td><td align=center>%s</td><td align=center>%s</td><td align=center>%s</td><td align=center><a href='deleteuser.py?uid=%s'>Delete</a></td></tr>"%(uid,uname,umobile,uemail,uid)
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
                                  
