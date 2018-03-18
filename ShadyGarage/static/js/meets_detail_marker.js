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
       styles: [
{
    "featureType": "all",
    "elementType": "labels.text.fill",
    "stylers": [
        {
            "color": "#ffffff"
        }
    ]
},
{
    "featureType": "all",
    "elementType": "labels.text.stroke",
    "stylers": [
        {
            "color": "#000000"
        },
        {
            "lightness": 13
        }
    ]
},
{
    "featureType": "administrative",
    "elementType": "geometry.fill",
    "stylers": [
        {
            "color": "#000000"
        }
    ]
},
{
    "featureType": "administrative",
    "elementType": "geometry.stroke",
    "stylers": [
        {
            "color": "#144b53"
        },
        {
            "lightness": 14
        },
        {
            "weight": 1.4
        }
    ]
},
{
    "featureType": "administrative.locality",
    "elementType": "all",
    "stylers": [
        {
            "visibility": "on"
        }
    ]
},
{
    "featureType": "administrative.locality",
    "elementType": "labels.icon",
    "stylers": [
        {
            "visibility": "on"
        }
    ]
},
{
    "featureType": "landscape",
    "elementType": "all",
    "stylers": [
        {
            "color": "#08304b"
        }
    ]
},
{
    "featureType": "poi",
    "elementType": "geometry",
    "stylers": [
        {
            "color": "#0c4152"
        },
        {
            "lightness": 5
        }
    ]
},
{
          featureType: 'road.highway',
          elementType: 'geometry.stroke',
          stylers: [{color: '#1f2835'}]
        },
        {
          featureType: 'road.highway',
          elementType: 'labels.text.fill',
          stylers: [{color: '#f3d19c'}]
        },
{
    "featureType": "road.arterial",
    "elementType": "geometry.fill",
    "stylers": [
        {
            "color": "#000000"
        }
    ]
},
{
    "featureType": "road.arterial",
    "elementType": "geometry.stroke",
    "stylers": [
        {
            "color": "#0b3d51"
        },
        {
            "lightness": 16
        }
    ]
},
{
    "featureType": "road.local",
    "elementType": "geometry",
    "stylers": [
        {
            "color": "#000000"
        }
    ]
},
{
    "featureType": "transit",
    "elementType": "all",
    "stylers": [
        {
            "color": "#146474"
        }
    ]
},
{
    "featureType": "water",
    "elementType": "all",
    "stylers": [
        {
            "color": "#021019"
        }
    ]
},
{
    featureType: "administrative.country",
    elementType: "geometry.stroke",
    stylers: [
        { color: "#FF0000" }
    ]
  },
]
     });

   }