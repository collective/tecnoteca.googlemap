// == refresh map position and marker ==
function refreshMarkerPosition(point) {		
	marker.setPosition(point);
    map.panTo(point);
    
    if (coordFieldId && coordFieldId!="") { // if edit mode
    	document.getElementById(coordFieldId).value = point.lat().toFixed(5) + "|" + point.lng().toFixed(5);
    }
}


// == disableCoordinates ==
function disableCoordinates() {
	var point = new google.maps.LatLng(0,0);
	refreshMarkerPosition(point);
}


// == search address (marker edit map) ==
function searchAddress(address) {
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( {'address': address}, function(results,status) {
        if (status == google.maps.GeocoderStatus.OK) {
	        var point = results[0].geometry.location;        
	        refreshMarkerPosition(point);
        } else {
            errpopup(ERRCODES['G_GEO_UNKNOWN_ADDRESS']);
        }
    });
}

//== disable enter ==
function disableEnterKey(e) {
     var key;     
     if(window.event)
          key = window.event.keyCode; // IE
     else
          key = e.which; // firefox
     return (key != 13);
}