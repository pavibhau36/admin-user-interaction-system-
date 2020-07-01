import MySQLdb
import cgi
form=cgi.FieldStorage()
sessid=form.getvalue("uid")
db=MySQLdb.connect("localhost","root","","mysqldb")
if db:
    cursor=db.cursor()
    selectQuery="select * from tb1_register where userid=%d"%(int(sessid))
    cursor.execute(selectQuery)
    results=cursor.fetchone()
    uid=results[0]
    uname=results[1]
    fname=results[2]
    lname=results[3]
    upwd=results[4]
    ucpwd=results[4]
    umobile=results[5]
    uemailid=results[6]
    ucountry=results[7]
    ustate=results[8]
    ucity=results[9]
    udob=results[10]
    udateofbirth=udob.split("-")
    uaddress=results[11]
    ugender=results[12]
        
    
    
    
    
print "<div id='container'>"
print "<div id='header'>"
print "<br>"
print "<center><font color=white><h1>UPDATE DETAILS</h1></font></center>"
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
print "<div id='leftpane'>"

print "<table width='60%' height='40%' align=center border=0>"
print "<tr><th align=center>Update My Profile</th></tr>"
print "<tr><td align=center><input type='text' name='uname' id='uname' placeholder='Enter UserName' title='Enter UserName' value='%s' required onKeyPress='return onlyAlphabet(event);'><input type='hidden' name='userid' id='userid' value='%s'> </td></tr>"%(uname,uid)
print "<tr><td align=center><input type='text' name='fname' placeholder='Enter FirstName' title='Enter FirstName' required value='%s'> </td></tr>"%(fname)
print "<tr><td align=center><input type='text' name='lname' placeholder='Enter LastName' title='Enter LastName' required value='%s'> </td></tr>"%(lname)
print "<tr><td align=center><input type='password' name='upwd' placeholder='Enter Password' title='Enter Password' required value='%s'> </td></tr>"%(upwd)
print "<tr><td align=center><input type='password' name='ucpwd' placeholder='Enter Confrim Password' title='Enter Confirm Password' value='%s' required onBlur='return checkPassword();'> </td></tr>"%(ucpwd)
print "<tr><td align=center><input type='text' name='umobile' id='umobile' placeholder='Enter Mobile Number' title='Enter Mobile Number' minlength=10 maxlength=12 required onKeyPress='return onlyNumber(event);' value='%s'> </td></tr>"%(umobile)
print "<tr><td align=center><input type='text' name='uemail' placeholder='Enter Email ' title='Enter Email' required onBlur='return checkEmail();' value='%s'> </td></tr>"%(uemailid)

print "</table>"
print "</div>"
print "<div id='rightpane'>"
print "<br>"
print "<table width='100%' height='60%' border=0>"
print "<tr><td align=center><select name='ucountry' id='ucountry' onChange='return pickCountry();'>"
print "<option value='%s' selected>%s</option>"%(ucountry,ucountry)
print "<option value='0'>---Select Country---</option>"
print "</select></td>"
print "<td align=center><select name='ustate' id='ustate' disabled onChange='return pickState();'>"
print "<option value='%s'>%s</option>"%(ustate,ustate)
print "<option value='0'>---Select State---</option>"
print "</select></td>"
print "<td align=center><select name='ucity' id='ucity' disabled>"
print "<option value='%s'>%s</option>"%(ucity,ucity)
print "<option value='0'>---Select City---</option>"
print "</select></td>"
print  "</tr>"

print "<tr><td align=center><select name='udate'>"
print "<option value='%s' selected>%s</option>"%(udateofbirth[0],udateofbirth[0])
print "<option value='0'>---Select Date---</option>"
for i in range(1,31+1):
    print "<option value=%d>%d</option>"%(i,i)
print "</select></td>"
print "<td align=center><select name='umonth'>"
print "<option value='%s' selected>%s</option>"%(udateofbirth[1],udateofbirth[1])
print "<option value='0'>---Select Month---</option>"
list=["January","Febraury","March","April","May","June","July","August","September","October","November","December"]
for j in range(12):
    print "<option value=%s>%s</option>"%(list[j],list[j])
print "</select></td>"
print "<td align=center><select name='uyear'>"
print "<option value='%s' selected>%s</option>"%(udateofbirth[2],udateofbirth[2])
print "<option value='0'>---Select Year---</option>"
for k in  range(2000,2050):
    print "<option value=%d>%d</option>"%(int(k),int(k))
print "</select></td>"
print  "</tr>"
print "<tr><td  colspan=3><textarea rows=5 cols=25 name='uaddress' value='%s'>%s</textarea></td></tr>"%(uaddress,uaddress)
if ugender=='Male':
    print "<tr><td  colspan=3>Select Gender<input type=radio name='ugender' value='Male' checked>Male &nbsp;&nbsp;<input type=radio name='ugender' value='Female'>Female</td></tr>"
if ugender=='Female':
    print "<tr><td  colspan=3>Select Gender<input type=radio name='ugender' value='Male'>Male &nbsp;&nbsp;<input type=radio name='ugender' value='Female' checked>Female</td></tr>"
print "<tr><td colspan=3><input type='file' name=ufile></td></tr>"
print "<tr><td colspan=3 align=center><input type='submit' name='rbutton' value='Update'> &nbsp;&nbsp;&nbsp;&nbsp;<input type='reset' name='resetbutton' value='Clear'></td></tr>"



print "</table>"
print "</div>"
print "<div id='footer'>"
print "<br>"
print "<center> <font color=white>&copy;Reserved to Company</font></center>"
print "</div>"
print "</div>"
