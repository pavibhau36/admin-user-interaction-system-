print "<div id='container'>"
print "<div id='header'>"
print "<br>"
print "<center><font color=white><h1>PERSONAL DETAILS MANAGEMENT SYSTEM</h1></font></center>"
print "</div>"
print "<div id='menubar'>"
##print "<table width='100%' border=0 id=menutable> <tr> <td align=center><a href='index.py'>HOME</a></td>"
##print "<td align=center><a href='aboutus.py'>aboutus</a></td>"
##print "<td align=center><a href='services.py'>services</a></td>"
##print "<td align=center><a href='gallery.py'>gallery</a></td>"
##print "<td align=center><a href='contactus.py'>contactus</a></td>"
##print "</tr>"
##print "</table>"
print "<ul><li><a href='layout.py'>Home</a></li>"
print "<li><a href='aboutus.py'>About Us</a></li>"
print "<li class='dropdown'>"
print "<a href='javascript:void(0)' class='drpbtn'>Services</a>"
print "<div class='dropdown-content'>"
print "<a href='webdesign.py'>Web Design</a>"
print "<a href='webdevelopment.py'>Web Development</a>"
print "</div></li>"
print "<li><a href='gallery.py'>Gallery</a></li>"
print "<li><a href='contactus.py'>Contact Us</a></li>"
print "</ul>"
print "</div>"
print "<div id='leftpane'>"
print "<br><br>"
print "<center><img src='idea-loading.jpg' width='200px' height='150px'></center>"
print "</div>"
print "<div id='rightpane'>"
print "<br><br>"
print "<table width='40%' height='40%' align=center border=0>"
print "<tr><th align=center>SignIn with ur account </th></tr>"
print "<tr><td align=center><input type='text' name='uname' placeholder='enter name' title='enter username' required></td></tr>"
print "<tr><td align=center><input type='password' name='upwd' placeholder='enter password' title='enter password' required ></td></tr>"
print "<tr><td align=center><input type='submit' name='ubutton' value='login'></td></tr>"
print "<tr><td align=center>If forget<a href='forgot.py'>password</a></td></tr>"
print "<tr><td align=center>if new user <a href='signup.py'>Sign up here </a></td></tr>"
print "</table>"
print "</div>"
print "<div id='footer'>"
print "<br>"
print "<center><font color=white>&copy;Reserved to company</center></font>"
print "</div>"
print "</div>"

