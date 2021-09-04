var next=document.getElementById("next");
next.addEventListener("click",function(){
    phonenumber=document.forms["register"]["phone number"].value
    fname=document.forms["register"]["first name"].value
    sname=document.forms["register"]["shop name"].value
    p1=document.forms["register"]["password1"].value
    p2=document.forms["register"]["password2"].value
    if(phonenumber!=='' && fname!=='' && sname!=='' && p1!=='' && p2!==''){
        f=document.getElementById("input");
    console.log(f);
    f.style.display="None"
    next.style.display="none"
    document.getElementById("staffpass").style.display="block"
    }
    
});

p=document.getElementById("phonenumber");
p.addEventListener("change",function(){
    phone=p.value;
    $.ajax({
        type:"GET",
        url:`/check/${phone}/`,
        success: function(status){
            if(status.status=="OK")
            {
            $("#msg").text(status.status)
            $("#msg").attr("class","alert-success")
            $("#msg").show()
            }
            else{
                $("#msg").text(status.status)
                $("#msg").show()
            }
        }
    });
});