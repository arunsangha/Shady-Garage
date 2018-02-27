function initMap() {
   var oslo = {lat: 59.913, lng: 10.752};
   var map = new google.maps.Map(document.getElementById('map'), {
     zoom: 6,
     center: oslo
   });
   var marker = new google.maps.Marker({
     position: oslo,
     map: map
   });
}

$(document).ready(function() {
$(".burger-nav").on('click', function() {
   $("div ul").toggleClass("nav-list-open");
});
});


















//TODO sjekk om dette funker
// const burgerNav = document.querySelector(".burger-nav");
//
// burgerNav.addEventListener("blur", hideBurgerWhenClickElsewhere);
//
// function hideBurgerWhenClickElsewhere(e){
//      burgerNav.classList.remove("nav-list-open");
// }
