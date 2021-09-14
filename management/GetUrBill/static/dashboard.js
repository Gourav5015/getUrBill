function logout(){
   window.location.pathname=("/logout/");

};
function load(){
   document.getElementById("load-img").style.display="flex";
};
document.getElementById("add").addEventListener("click",function(){
   item=document.forms["form"]["item_name"].value
   quantity=document.forms["form"]["quantity"].value
   price=document.forms["form"]["price"].value
   discount=document.forms["form"]["discount"].value
   if(item!=='' && quantity!=='' && price!=='' && discount!=='')
   {
      load()
   }

})
