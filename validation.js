function onCountry()
{
	
var select=document.getElementById("ucountry");

var options=["Australia","Newzealand","England","India","Pakistan"];
for(var i=0;i<options.length;i++)
{
	var opt=options[i];
	var e1=document.createElement("option");
	e1.textContent=opt;
	e1.value=opt;
	select.appendChild(e1);
	
}
}
function pickCountry()
{
selectedCountry=document.register.ucountry.value;
if(selectedCountry=="India")
{
document.register.ustate.disabled=false
state=document.getElementById("ustate");
var options=["TamilNadu","Karnataka","Kerala","Hyderabad"];
for(var i=0;i<options.length;i++)
{
	var opt=options[i];
	var e1=document.createElement("option");
	e1.textContent=opt;
	e1.value=opt;
	state.appendChild(e1);
}
}
else
{
	alert("select only India");
	document.register.ustate.disabled=true;
}
}



function pickState()
{
selectedState=document.register.ustate.value;
if(selectedState=="TamilNadu")
{
document.register.ucity.disabled=false
city=document.getElementById("ucity");
var options=["Coimbatore","Tirupur","Erode","Vellore"];
for(var i=0;i<options.length;i++)
{
	var opt=options[i];
	var e1=document.createElement("option");
	e1.textContent=opt;
	e1.value=opt;
	city.appendChild(e1);
}
}
else
{
	alert("select only TamilNadu");
	document.register.ucity.disabled=true;
}
}


function onlyAlphabet(evt)
{
    
    var charCode=(evt.which)?evt.which:evt.keyCode;
     if((charCode>64 && charCode<91) || (charCode>96 && charCode<123))
    {
        return true;
        }
    else
        {
    alert("Only Alphabtes allowed")
            document.getElementById('uname').style.backgroundColor="red" 
        return false;
         }
    }


function onlyNumber(evt)
{
    var ikeyCode=(evt.which)?evt.which:evt.keyCode;
    if((ikeyCode!=46 && ikeyCode>31) && (ikeyCode<48 || ikeyCode>57))
{
    alert("Only Number allowed")
    document.getElementById('umobile').style.backgroundColor="red"
          return false;
    }
    else
    {
        return true;
        }
  }

function checkPassword()
{
    upwd=document.register.upwd.value;
    ucpwd=document.register.ucpwd.value;
    if(upwd==ucpwd)
    {
        return true;
        }
    else
    {
        alert("Password is Mismatching");
        return false;
        }
    }
function checkEmail()
{
    
    uemail=document.register.uemail.value;   
    dotpos=uemail.lastIndexOf('.')
    atpos=uemail.indexOf('@')
    
    if(dotpos==-1 || atpos==-1 || dotpos-atpos<=4)
    {
        alert("invalid format of Email Id")
         
        return false     ; 
        }
    else
        {
            return true;
            }

    
    
    }
