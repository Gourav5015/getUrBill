a=document.querySelector("#addbutton");
console.log(a)
a.addEventListener('click',function(){
    itemname=document.forms['additem']['itemselected'].value
    quantity=document.forms['additem']['quantity'].value
    csrf=document.forms['additem']['csrfmiddlewaretoken'].value
    billnumb=document.forms['additem']['bill number'].value
    console.log(itemname,quantity,csrf,billnumb)
});


