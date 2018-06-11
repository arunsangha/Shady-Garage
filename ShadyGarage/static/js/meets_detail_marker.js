function initMap(){
     var geocoder = new google.maps.Geocoder();
     var location = document.getElementById('location').textContent;
     var markerIcon = document.getElementById("location").getAttribute("data-marker")
     var oslo = {lat: 59.913, lng: 10.752};
     var directionsService = new google.maps.DirectionsService();
     var directionsDisplay = new google.maps.DirectionsRenderer();
     var marker, placeid, contentString, infowindow;
     geocoder.geocode({'address':location}, function(results, status){
       if(status === google.maps.GeocoderStatus.OK){
           map.setCenter(results[0].geometry.location);
           placeid = results[0].place_id;
           lat = results[0].geometry.location.lat();
           long = results[0].geometry.location.lng();

           contentString = '<div id="content">'+
                   '<a href="#" onclick="mapSelector(event)" data-location="' + location + '"data-placeid="' + placeid +'" data-lat="' + lat + '" data-long="'+ long+'"class="btn btn-info" id="navigationButton">Ta meg hit</a></div>';


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


function mapSelector(e){
  e.preventDefault();
  var placeid = document.getElementById("navigationButton").getAttribute("data-placeid");
  var lat = document.getElementById("navigationButton").getAttribute("data-lat");
  var long = document.getElementById("navigationButton").getAttribute("data-long");
  var location = document.getElementById("navigationButton").getAttribute("data-location");
  console.log(placeid);
  console.log(lat)
  console.log(long)
  var ua = navigator.userAgent.toLowerCase();
  var isAndroid = ua.indexOf("android") > -1; //&& ua.indexOf("mobile");

  var url = "";
  /* if we're on iOS, open in Apple Maps */
  if ((navigator.platform.indexOf("iPhone") != -1) || (navigator.platform.indexOf("iPad") != -1) || (navigator.platform.indexOf("iPod") != -1)){
      url = "comgooglemaps://?q=" + location;
        window.open(url);
  }else if(isAndroid){
    window.location = "https://www.google.com/maps/place/?q=place_id:" + placeid;
  }else{
      url = "https://www.google.com/maps/place/?q=place_id:" + placeid;
      window.open(url);
  }

}
