function initMap() {
     var geocoder = new google.maps.Geocoder();
     var location = document.getElementById('location').textContent;
     console.log("Location: " + location)
     var oslo = {lat: 59.913, lng: 10.752};
     var directionsService = new google.maps.DirectionsService();
     var directionsDisplay = new google.maps.DirectionsRenderer();
     geocoder.geocode({'address':location}, function(results, status){
       console.log(results)
       console.log(status)
       if(status === google.maps.GeocoderStatus.OK){
         map.setCenter(results[0].geometry.location);
         var marker = new google.maps.Marker({
           map:map,
           position: results[0].geometry.location,
           zoom: 10,
         })
       }else{
         console.log("ERROR I MAP")
       }
     })
     var map = new google.maps.Map(document.getElementById('map'), {
       zoom: 15,
       center: oslo,
     });

   }

   $(document).ready(function() {
   	$(".burger-nav").on('click', function() {
   		$("div ul").toggleClass("nav-list-open");
   	});
   });
/*
TODO: Må aktivere googlemaps geocode i christan sin apikey.

fra google api:

var geocoder;
 var map;
 function initialize() {
   geocoder = new google.maps.Geocoder();
   var latlng = new google.maps.LatLng(-34.397, 150.644);
   var mapOptions = {
     zoom: 8,
     center: latlng
   }
   map = new google.maps.Map(document.getElementById('map'), mapOptions);
 }

 function codeAddress() {
   var address = document.getElementById('address').value;
   geocoder.geocode( { 'address': address}, function(results, status) {
     if (status == 'OK') {
       map.setCenter(results[0].geometry.location);
       var marker = new google.maps.Marker({
           map: map,
           position: results[0].geometry.location
       });
     } else {
       alert('Geocode was not successful for the following reason: ' + status);
     }
   });
 }

<body onload="initialize()">
<div id="map" style="width: 320px; height: 480px;"></div>
 <div>
   <input id="address" type="textbox" value="Sydney, NSW">
   <input type="button" value="Encode" onclick="codeAddress()">
 </div>
</body>



*/



//TODO sjekk om dette funker
// const burgerNav = document.querySelector(".burger-nav");
//
// burgerNav.addEventListener("blur", hideBurgerWhenClickElsewhere);
//
// function hideBurgerWhenClickElsewhere(e){
//      burgerNav.classList.remove("nav-list-open");
// }
