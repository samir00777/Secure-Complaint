function myRoleChange()
{
document.getElementById("student").style.display = "none";
document.getElementById("teacher").style.display = "none";
document.getElementById("head").style.display = "none";
document.getElementById(role.value).style.display = "block";
}

function againstRoleChange()
{
document.getElementById("astudent").style.display = "none";
document.getElementById("ateacher").style.display = "none";
document.getElementById("ahead").style.display = "none";
document.getElementById("a" + against.value).style.display = "block";
}

function toRoleChange()
{
document.getElementById("toteacher").style.display = "none";
document.getElementById("tohead").style.display = "none";
document.getElementById("to" + to_role.value).style.display = "block";
}