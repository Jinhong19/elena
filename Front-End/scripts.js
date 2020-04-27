

//////////////////////
function myFunction() {

// var startLatLong = [0.0, 0.0];
// var endLatLong = [0.0, 0.0];

var startValue = document.getElementById("startlocation").value;
var endValue = document.getElementById("endlocation").value;
var sPercentage = document.getElementById("percentageofshortestdistance").value;
var minMax = document.getElementById("minmax").value;

// Send request to server
// response format: data = {start: Boston, end: Amherst, route: [{lat: 71.32, lon:21.1231}, {lat: 12.12, lon: 22.12}]}
// access: data.routes[0].lat

const url = 'http://localhost:5000/positions'
console.log('fetching with ' + url);
let data = {start: startValue, end: endValue, percentage: sPercentage, mM: minMax};
fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
    .then(res => res.json())
    .then(data => {
        var storeData = [];
        if(data.start.localeCompare(startValue) == 0 && data.end.localeCompare(endValue) == 0){
            for(var i = 0; i<data.route.length; i++){
                    storeData.push(L.latLng(data.route[i].lat, data.route[i].lon));
                }
            }
            
        var map = L.map('mapid').setView([0,0], 2);
        
        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww', {
             attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
             maxZoom: 18,
             id: 'mapbox/streets-v11',
             tileSize: 512,
             zoomOffset: -1,
         }).addTo(map);
    
        L.Routing.control({
            waypoints: storeData,
            routeWhileDragging: true,
            router: L.Routing.mapbox('pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww'),
            geocoder: L.Control.Geocoder.nominatim(),
            waypointMode: 'snap',
            createMarker: function() {}
        }).addTo(map);
    }
)


// put the data=> into your function

// fetch('./fake.json')
//   .then(response => {
//     return response.json()
//   })
//   .then(data => {
//     var storeData = [];
//     if(data.start.localeCompare(startValue) == 0 && data.end.localeCompare(endValue) == 0){
//         for(var i = 0; i<data.route.length; i++){
//                 storeData.push(L.latLng(data.route[i].lat, data.route[i].lon));
//             }
//         }

//     var map = L.map('mapid').setView([0,0], 2);
    
//     L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww', {
//          attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//          maxZoom: 18,
//          id: 'mapbox/streets-v11',
//          tileSize: 512,
//          zoomOffset: -1,
//      }).addTo(map);

//     L.Routing.control({
//         waypoints: storeData,
//         routeWhileDragging: true,
//         router: L.Routing.mapbox('pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww'),
//         geocoder: L.Control.Geocoder.nominatim(),
//         waypointMode: 'snap',
//         createMarker: function() {}
//     }).addTo(map);
//   })
//   .catch(err => {
//     // Do something for an error here
//   })

return false;
};






////////////////////////////////////

