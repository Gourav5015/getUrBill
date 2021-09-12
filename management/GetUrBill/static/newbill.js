a=document.querySelector("#addbutton");
console.log(a)
a.addEventListener('click',function(){
    itemname=document.getElementById("itemselected").value
    quantity=document.getElementById("quantity").value
    billnumb=document.getElementById("billnumber").value
    console.log(itemname,quantity,billnumb)
    $.ajax({url:'/ajaxitem/',
    type:'POST',
    data:`{"itemselected":"${itemname}","quantity":"${quantity}","billnumber":"${billnumb}"}`,
    contentType: 'application/json',
    dataType:'json',
    success:
    function(data){
        console.log(data)
      table=document.getElementById("id_of_table")
      table.innerHTML=""
      tr=document.createElement("tr")
      s=document.createElement("th")
      i=document.createElement("th")
      p=document.createElement("th")
      d=document.createElement("th")
      f=document.createElement("th")
      s.innerText="sl no."
      i.innerText="itemname"
      p.innerText="price"
      d.innerText="discount"
      f.innerText="final price"
      table.appendChild(tr)
      table.appendChild(s)
      table.appendChild(i)
      table.appendChild(p)
      table.appendChild(d)
      table.appendChild(f)

        data.items.forEach((d,counter)=>{
            serialno=document.createElement("td")
            serialno.innerText=counter+1
            itemname=document.createElement("td")
            itemname.innerText=d.itemname
            price=document.createElement("td")
            price.innerText=d.price
            discount=document.createElement("td")
            discount.innerText=d.discount
            finalprice=document.createElement("td")
            finalprice.innerText=d.Final_Price
           tr=document.createElement("tr")
            
            table.appendChild(tr)
            table.appendChild(serialno)
            table.appendChild(itemname)
            table.appendChild(price)
            table.appendChild(discount)
            table.appendChild(finalprice)
        
        })
        console.log(data.Total_Price)
total=document.getElementById("total")        
        total.innerText=`total price:${data.Total_Price}`
    } });
});
