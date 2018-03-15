function initMap() {
     var geocoder = new google.maps.Geocoder();
     var location = document.getElementById('location').textContent;
     var markerIcon = document.getElementById("location").getAttribute("data-marker")
     console.log(markerIcon)
     console.log("Location: " + location)
     var oslo = {lat: 59.913, lng: 10.752};
     var directionsService = new google.maps.DirectionsService();
     var directionsDisplay = new google.maps.DirectionsRenderer();
     var marker, placeid, contentString, infowindow;
     geocoder.geocode({'address':location}, function(results, status){
       console.log(results)
       console.log(status)
       if(status === google.maps.GeocoderStatus.OK){
           map.setCenter(results[0].geometry.location);
           placeid = results[0].place_id;
           contentString = '<div id="content">'+
                   '<a href="https://www.google.com/maps/place/?q=place_id:' + placeid +'"target="_blank" class="btn btn-info">Ta meg hit</a></div>';



           marker = new google.maps.Marker({
             map:map,
             position: results[0].geometry.location,
             zoom: 10,
             icon: "../../../" + markerIcon,
           });

           infowindow = new google.maps.InfoWindow({
             content: contentString,
            maxWidth: 100
           });

           marker.addListener('click', function(){
             infowindow.open(map, marker);
           });

       }else{
         console.log("ERROR I MAP")
       }
     })
     var map = new google.maps.Map(document.getElementById('map'), {
       zoom: 15,
       center: oslo,
     });

   }
