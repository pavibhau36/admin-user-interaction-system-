print "<div id='container'>"
print "<div id='header'>"
print "<br>"
print "<center><font color=white><h1>REGISTRATION</h1></font></center>"
print "</div>"
print "<div id='menubar'>"
print "<table width='100%' border=0 id=menutable><tr><td align=center><a href='index.py'>Home</a></td>"
print "<td align=center><a href='aboutus.py'>About Us</a></td>"
print "<td align=center><a href='services.py'>Services</a></td>"
print "<td align=center><a href='galler.py'>Gallery</a></td>"
print "<td align=center><a href='contactus.py'>Contact Us</a></td>"
print  "</tr>"
print "</table>"
print "</div>"
print "<div id='leftpane'>"
print "<table width='60%' height='40%' align=center border=0>"
print "<tr><th align=center>Register Here</th></tr>"
print "<tr><td align=center><input type='text' name='uname' id='uname' placeholder='Enter UserName' title='Enter UserName' required onKeyPress='return onlyAlphabet(event);'> </td></tr>"
print "<tr><td align=center><input type='text' name='fname' placeholder='Enter FirstName' title='Enter FirstName' required> </td></tr>"
print "<tr><td align=center><input type='text' name='lname' placeholder='Enter LastName' title='Enter LastName' required> </td></tr>"
print "<tr><td align=center><input type='password' name='upwd' placeholder='Enter Password' title='Enter Password' required> </td></tr>"
print "<tr><td align=center><input type='password' name='ucpwd' placeholder='Enter Confirm Password' title='Enter Confirm Password' required onBlur='checkPassword()'> </td></tr>"
print "<tr><td align=center><input type='text' name='umobile' id='umobile' placeholder='Enter Mobile Number' title='Enter Mobile Number' minlength=10 maxlength=12 required onKeyPress='return onlyNumber(event);'> </td></tr>"
print"<tr><td align=center><input type='text' name='uemail' placeholder='Enter Email ' title='Enter Email' required onBlur='return checkEmail();'> </td></tr>"

print "</table>"
print "</div>"
print "<div id='rightpane'>"
print "<br>"
print "<table width='100%' height='60%' border=0>"
print "<tr><td align=center><select name='ucountry' id='ucountry' onChange='return pickCountry();'>"
print "<option value='0'>---Select Country---</option>"
print "</select></td>"
print "<td align=center><select name='ustate' id='ustate' disabled onChange='return pickState();'>"
print "<option value='0'>---Select State---</option>"
print "</select></td>"
print "<td align=center><select name='ucity' id='ucity' disabled>"
print "<option value='0'>---Select City---</option>"
print "</select></td>"
print  "</tr>"
print "<tr><td align=center><select name='udate'>"
print "<option value='0'>---Select Date---</option>"
for i in range(1,31+1):
    print "<option value=%d>%d</option>"%(i,i)
print "</select></td>"
print "<td align=center><select name='umonth'>"
print "<option value='0'>---Select Month---</option>"
list=["January","Febraury","March","April","May","June","July","August","September","October","November","December"]
for j in range(12):
    print "<option value=%s>%s</option>"%(list[j],list[j])
print "</select></td>"
print "<td align=center><select name='uyear'>"
print "<option value='0'>---Select Year---</option>"
for k in  range(2000,2050):
    print "<option value=%d>%d</option>"%(int(k),int(k))
print "</select></td>"
print  "</tr>"
print "<tr><td  colspan=3><textarea rows=5 cols=25 name='uaddress'></textarea></td></tr>"
print "<tr><td  colspan=3>Select Gender<input type=radio name='ugender' value='Male'>Male &nbsp;&nbsp;<input type=radio name='ugender' value='Female'>Female</td></tr>"
print "<tr><td colspan=3><input type='file' name='ufile'></td></tr>"
print "<tr><td colspan=3><input type='checkbox' name=utoc value=TOC>I Accept the Terms & Conditions</td></tr>"
print "<tr><td colspan=3 align=center><input type='submit' name='rbutton' value='Signup'> &nbsp;&nbsp;&nbsp;&nbsp;<input type='reset' name='resetbutton' value='Clear'></td></tr>"
print "<tr><td colspan=3 align=center><a href='index.py'>If Already Registered Click Here</a></td></tr>"


print "</table>"
print "</div>"
print "<div id='footer'>"
print "<br>"
print "<center> <font color=white>&copy;Reserved to Company</font></center>"
print "</div>"
print "</div>"
