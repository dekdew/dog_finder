latitude = document.getElementById('id_latitude');
longtitude = document.getElementById('id_longtitude');

latitude.value = 13.7278245;
longtitude.value = 100.77911;

mapboxgl.accessToken = 'pk.eyJ1IjoicGFzc2F3aXQiLCJhIjoiY2p2ZTJhdnl4MTczazQxcDg4Zzk5ZnZxMyJ9.7teQ6On47tRGb06Nz0_oUA';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [100.77911, 13.7278245],
    zoom: 13
});

var marker = new mapboxgl.Marker({
    draggable: true,
    color: '#ffbb33'
})
    .setLngLat([100.77911, 13.7278245])
    .addTo(map);

function onDragEnd() {
    var lngLat = marker.getLngLat();
    longtitude.value = lngLat.lng;
    latitude.value = lngLat.lat;
}

marker.on('dragend', onDragEnd);

var geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    marker: null,
    mapboxgl: mapboxgl
});

map.addControl(geocoder);

// Add geolocate control to the map.
var geolocate = new mapboxgl.GeolocateControl({
    positionOptions: {
        enableHighAccuracy: true
    },
    showUserLocation: false,
    trackUserLocation: true
});

map.addControl(geolocate);

geolocate.on('geolocate', function (e) {
    lat = e.coords.latitude;
    lng = e.coords.longitude;
    marker.setLngLat([lng, lat]);
    longtitude.value = lng;
    latitude.value = lat;
});

geocoder.on('result', function (e) {
    marker.setLngLat(e.result.geometry.coordinates);
    longtitude.value = e.result.geometry.coordinates[0];
    latitude.value = e.result.geometry.coordinates[1];
});

map.on('click', function (e) {
    marker.setLngLat(e.lngLat);
    longtitude.value = e.lngLat.lng;
    latitude.value = e.lngLat.lat;
});
