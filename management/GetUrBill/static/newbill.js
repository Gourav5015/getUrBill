a=document.querySelector("#addbutton");
console.log(a)
a.addEventListener('click',function(){
    itemname=document.forms['additem']['itemselected'].value
    quantity=document.forms['additem']['quantity'].value
    csrf=document.forms['additem']['csrfmiddlewaretoken'].value
    billnumb=document.forms['additem']['billnumber'].value
    console.log(itemname,quantity,csrf,billnumb)
    $.ajax({url:'/ajaxitem/',
    type:'POST',
    data:`{'itemselected':${itemname},'quantity':${quantity},'csrfmiddlewaretoken':${csrf},'billnumber':${billnumb}}`,
    contentType: 'application/json',
    dataType:'json',
    success:
    function(data){
        console.log(data)
    } });
});
