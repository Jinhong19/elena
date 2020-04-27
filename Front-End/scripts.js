

//////////////////////
function myFunction() {

var startLatLong = [0.0, 0.0];
var endLatLong = [0.0, 0.0];

var startValue = document.getElementById("startlocation").value;
var endValue = document.getElementById("endlocation").value;
let persentage = document.getElementById("").value

// Send request to server
// response format: data = {start: Boston, end: Amherst, route: [{lat: 71.32, lon:21.1231}, {lat: 12.12, lon: 22.12}]}
// access: data.routes[0].lat
const url = 'http://localhost:5000/positions'
console.log('fetching with ' + url)
let data = {start: startValue, end: endValue}
fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
    .then(res => res.json())
    .then(data => {
        console.log(data)
    }
)

if(startValue.localeCompare("boston") == 0){
        startLatLong[0] = 42.340382; startLatLong[1] = -71.496819;
}

if(endValue.localeCompare("amherst") == 0){
        endLatLong[0] = 42.340382; endLatLong[1] = -71.057083
}



var map = L.map('mapid').setView([0,0], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww', {
     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
     maxZoom: 18,
     id: 'mapbox/streets-v11',
     tileSize: 512,
     zoomOffset: -1,
 }).addTo(map);

 //will have to find in database the values for start and end value
 // wavepoints would be latlang array  

L.Routing.control({
    waypoints: [
        L.latLng(startLatLong[0], startLatLong[1]),
        L.latLng(endLatLong[0], endLatLong[1]),
    ],
	routeWhileDragging: true,
    router: L.Routing.mapbox('pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww'),
    geocoder: L.Control.Geocoder.nominatim(),
    waypointMode: 'snap',
    createMarker: function() {}
}).addTo(map);

return false;
};






////////////////////////////////////

