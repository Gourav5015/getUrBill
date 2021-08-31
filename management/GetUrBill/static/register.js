var next=document.getElementById("next");
next.addEventListener("click",function(){
    f=document.getElementById("input");
    console.log(f);
    f.style.display="None"
    next.style.display="none"
    document.getElementById("staffpass").style.display="block"
});

