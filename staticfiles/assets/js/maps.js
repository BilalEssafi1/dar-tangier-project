// Google Maps Location
window.initMap = function() {
    const leopoldStr = { lat: 48.1618, lng: 11.5843 };
    const map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: leopoldStr
    });
    const marker = new google.maps.Marker({
        position: leopoldStr,
        map: map,
        title: "Leopoldstraße 50, Munich"
    });
}
