

$(document).ready(function() {
 $(".burger-nav").on('click', function() {
   $("div ul").toggleClass("nav-list-open");
 });
});

// //TODO sjekk om dette funker
// const navList = document.querySelector("div ul");
// const card = document.querySelector(".index-card");
//
// card.addEventListener("click", hideBurgerWhenClickElsewhere);
//
// function hideBurgerWhenClickElsewhere(e){
//      navList.classList.add("nav-list-open");
//      console.log("hello");
// }
//
// card.addEventListener("blur", hideBurgerWhenClickElsewhere);
//
// function hideBurgerWhenClickElsewhere(e){
//      navList.classList.remove("nav-list-open");
//      console.log("hello");
// }
