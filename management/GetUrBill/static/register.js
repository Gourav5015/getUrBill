var next=document.getElementById("next");
next.addEventListener("click",function(){
    f=document.getElementById("input");
    console.log(f);
    f.style.display="None"
    next.style.display="none"
    document.getElementById("staffpass").style.display="block"
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