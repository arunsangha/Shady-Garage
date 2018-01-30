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
