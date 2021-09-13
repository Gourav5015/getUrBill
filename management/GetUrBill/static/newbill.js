a=document.querySelector("#addbutton");
console.log(a)
a.addEventListener('click',function(){
    itemname=document.getElementById("itemselected").value
    quantity=document.getElementById("quantity").value
    billnumb=document.getElementById("billnumber").value
    max=document.getElementById("quantity").max
    contact=document.getElementById("contact").value
    console.log(max)
    if (Number(quantity)>Number(max)){
        quantity=max
        console.log(max)
    }
    $.ajax({url:'/ajaxitem/',
    type:'POST',
    data:`{"itemselected":"${itemname}","quantity":"${quantity}","billnumber":"${billnumb}"}`,
    contentType: 'application/json',
    dataType:'json',
    success:
    function(data){
      table=document.getElementById("id_of_table")
      table.innerHTML=""
      tr=document.createElement("tr")
      s=document.createElement("th")
      i=document.createElement("th")
      q=document.createElement("th")
      p=document.createElement("th")
      d=document.createElement("th")
      f=document.createElement("th")
      de=document.createElement("th")
      s.innerText="sl no."
      i.innerText="itemname"
      q.innerText="quantity"
      p.innerText="price"
      d.innerText="discount"
      f.innerText="final price"
      de.innerText="delete"
      table.appendChild(tr)
      table.appendChild(s)
      table.appendChild(i)
      table.appendChild(q)
      table.appendChild(p)
      table.appendChild(d)
      table.appendChild(f)
      table.appendChild(de)

        data.items.forEach((d,counter)=>{
            li=document.createElement("a")
            li.setAttribute("href",`/${contact}/${billnumb}/d/${d.id}`)
            li.innerText="delete"
            serialno=document.createElement("td")
            serialno.innerText=counter+1
            itemname=document.createElement("td")
            itemname.innerText=d.itemname
            quantity=document.createElement("td")
            quantity.innerText=d.quantity
            price=document.createElement("td")
            price.innerText=d.price
            discount=document.createElement("td")
            discount.innerText=d.discount
            finalprice=document.createElement("td")
            finalprice.innerText=d.Final_Price
            delet=document.createElement("td")
            delet.appendChild(li)
           tr=document.createElement("tr")
            
            table.appendChild(tr)
            table.appendChild(serialno)
            table.appendChild(itemname)
            table.appendChild(quantity)
            table.appendChild(price)
            table.appendChild(discount)
            table.appendChild(finalprice)
            table.appendChild(delet)
        
        })
        select=document.getElementById("itemselected")
        select.innerHTML=""
        n=document.createElement("option")
        n.setAttribute("value","none")
        n.innerText="select"
        select.appendChild(n)
        data.itemname.forEach((d)=>{
            n=document.createElement("option")
            n.setAttribute("value",d)
            n.innerText=d
            select.appendChild(n)
        })
        document.getElementById("itemselected").value='none'
        document.getElementById("quantity").value=''
        document.getElementById("quantity").disabled=true
        document.getElementById("addbutton").disabled=true
total=document.getElementById("total")        
        total.innerText=`total price:${data.Total_Price}`
        
    } });
});

item=document.getElementById("itemselected")
item.addEventListener("change",function(){
    if (item.value!=="none"){
        document.getElementById("quantity").value=''
        document.getElementById("quantity").disabled=true
        document.getElementById("addbutton").disabled=true
        $.ajax({
            url:`/checkquantity/${item.value}`,
            type:"GET",
            success:function(data){
                document.getElementById("quantity").setAttribute("max",data.quantity)
            }
        })
        document.getElementById("quantity").removeAttribute("disabled")
    }
    else{
        document.getElementById("quantity").disabled=true
    }
    
})
function check(){
    quan=document.querySelector("#quantity")
    if ( Number(quan.value) > Number(quan.max)){
        
        quan.value=quan.max;
    }
    document.getElementById("addbutton").disabled=false
}