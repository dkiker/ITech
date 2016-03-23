//Initialize map
var map;
var infowindow;
function initialize() {
    var glasgow = new google.maps.LatLng(55.873686,-4.2518197);
    var mapOptions = {
        zoom: 9,
        center: glasgow
    };

    map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

    infowindow = new google.maps.InfoWindow();


}

function generateContent(place) {

    return '<div id="content">' +
        '<h3 id="firstHeading" class="firstHeading">'+place.name+'</h3>' +
        '<div id="bodyContent">' +
        '<p>'+place.description+'</p>' +
        '<p>Add to visit list:<button type="button" class="glyphicon glyphicon-plus addplace" id='+place.id+' name="'+place.name+'" />' +
        '</div>' +
        '</div>';
}

function add_marker(markers){
    markers.forEach(function (entry){
        var imgType;
        switch (entry.type){
            case 'A': imgType="img/attraction.png";break;
            case 'H':imgType="img/hotel.png";break;
            case 'R':imgType="img/restaurant.png";break;
        }
        var marker = new google.maps.Marker({
            position: {"lat" :parseFloat(entry.lat), "lng": parseFloat(entry.lng)},
            map: map,
            title: 'Hello World!',
            icon: "../../assets/"+imgType
        });
        //marker.setMap(map);

        var content = generateContent(entry);
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.setContent(content);
            infowindow.open(map, this);
        });
    });
}

$(document).on('click', '.addplace', function () {
    $('#places').append($('<option>', {
        name: this.name,
        value: this.id,
        text: this.name,
        selected: true
    }));
});

$("#new-dest").click(function () {
    var geo = new google.maps.Geocoder;
    address = $("#new-dest-text").val();
    geo.geocode({'address': address}, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
        } else {
            alert("Geocode was not successful for the following reason: " + status);
        }

    });

    $.get('/triplanter/add_location/', {location: address}, function (data) {
        add_marker(data);
    });
});

$("#last").click(function () {
    $("#places").find('option:last-child').remove();
});
$("#all").click(function () {
    $("#places").empty();

});
