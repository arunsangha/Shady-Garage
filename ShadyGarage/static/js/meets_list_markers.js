function initMap() {
     var oslo = {lat: 63.74644, lng: 11.29963};
     var marker, placeid, contentString, infowindow;


    $(document).ready(function(){
      var meetsList = [];
      var nextUrl;
     $.ajax({
       method:'GET',
       url: '/../../api/meets/',
       success:function(data){
         var map = new google.maps.Map(document.getElementById('map'), {
           zoom: 5,
           center: oslo,
         });
         meetsList = data.results;
         nextUrl = data.nextUrl;
         $.each(meetsList, function(key, value){
           console.log(value.location)
           if(value.location){
             var geocoder = new google.maps.Geocoder();
             var location = value.location
             var marker, placeid, contentString, infowindow;

             geocoder.geocode({'address':location}, function(results, status){
               if(status === google.maps.GeocoderStatus.OK){
                   placeid = results[0].place_id;
                   contentString = '<div id="content">'+
                           '<a href="https://www.google.com/maps/place/?q=place_id:' + placeid +'"target="_blank" class="btn btn-info">Ta meg hit</a></div>';

                   marker = new google.maps.Marker({
                     map:map,
                     position: results[0].geometry.location,
                     icon: "../../../static/images/e30marker.svg",
                     size: (1, 1),
                   });

                   infowindow = new google.maps.InfoWindow({
                     content: contentString,
                    maxWidth: 100
                   });

                   marker.addListener('click', function(){
                     infowindow.open(map, marker);
                   });

               }else{
                 console.log("ERROR!->: MAP")
               }
             })
           }

         })
       },error:function(data){
         console.log("Error!->: in getting meets list markers")
       }
     })


     })
   }
