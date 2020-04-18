

//////////////////////
var map = L.map('mapid').setView([0,0], 2);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww', {
     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
     maxZoom: 18,
     id: 'mapbox/streets-v11',
     tileSize: 512,
     zoomOffset: -1,
 }).addTo(map);


 L.Routing.control({
    waypoints: [
        L.latLng(57.74, 11.94),
        L.latLng(57.6792, 11.949)
    ],
	routeWhileDragging: true,
	router: L.Routing.mapbox('pk.eyJ1IjoicG5hZ3JhaiIsImEiOiJjazkwZW05OGcwMHl1M2VtdXhoeG4xYTlwIn0.sIjAUDjbWKYkXGTYlKp8Ww')
}).addTo(map);
////////////////////////////////////

