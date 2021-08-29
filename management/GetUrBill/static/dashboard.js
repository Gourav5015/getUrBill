function logout(){
   window.location.pathname=("/logout/");

};

function dis(){
   el=document.getElementById("price");
   discount=document.getElementById("discount");
   discount.value=0.1*el.value;
};

form=document.getElementById("add");
form.addEventListener("click",function(){
   c=document.getElementById("count");
   console.log(c)
   c.value=Number(c.value)+1;
   var b=document.createElement("br")

   var item_name =document.createElement("input");
   item_name.setAttribute("tpye","text")
   item_name.setAttribute("name","item_name"+c.value)
   var quantity =document.createElement("input");
   quantity.setAttribute("type","number")
   quantity.setAttribute("name","quantity"+c.value)
   var discount =document.createElement("input");
   discount.setAttribute("type","number")
   discount.setAttribute("name","discount"+c.value)
   var price=document.createElement("input");
   price.setAttribute("type","number")
   price.setAttribute("onchange","dis()")
   price.setAttribute("name","price"+c.value)
   var gst =document.createElement("input");
   gst.setAttribute("type","number")
   gst.setAttribute("name","gst"+c.value)
   f=document.getElementById("form-group")
   f.append(b);
   f.append(item_name);
   f.append(quantity);
   f.append(discount);
   f.append(price);
   f.append(gst);
});