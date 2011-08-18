// JavaScript Document

// == Get image width/height ==
function getImgSize(imgSrc) {
    var newImg = new Image();
    newImg.src = imgSrc;
    var height = newImg.height;
    var width = newImg.width;
    return [height,width];
}

// == Create icon function ==
function createIcon(imgUrl) {
    var imgsize = getImgSize(imgUrl);    
    var icon = new GIcon(G_DEFAULT_ICON,imgUrl);
    if(imgsize[0]!=null && imgsize[0]!=0) { // if size defined
        icon.iconSize = new GSize(imgsize[1], imgsize[0]);
    } else { // set default
        icon.iconSize = new GSize(32,37);
    }
    icon.iconAnchor = new GPoint(16,34); // set anchor point
    icon.imageMap = [0,0, icon.iconSize.width,0, icon.iconSize.width,icon.iconSize.height, 0,icon.iconSize.height]; // set clickable area
    icon.shadowSize = new GSize(0, 0); // disable shadow
    return icon;
}

//== Create clusterer icon ==
function createClustererIcon(imgUrl) {
	var height = 37;
	var width = 32;
	var imgsize = getImgSize(imgUrl);
	if(imgsize[0]!=null && imgsize[0]!=0) { // if size defined
		height = imgsize[0];
		width = imgsize[1];
	}
	var clustererIcon = [{
		url: imgUrl,
        height: height,
        width: width,
        opt_anchor: [height, width],
        opt_textColor: '#FFFFFF'
    }];
	return clustererIcon;
}


// == Create marker ==
function createMarker(id,point,name,html,category,categoryFullName) {    
	var marker = new GMarker(point, {icon:gicons[category], title:name})
    // === Store the category and name info as a marker properties ===
    marker.myid = id;
    marker.mycategory = category;
    marker.mycategoryfullname = categoryFullName;
    marker.myname = name;
    GEvent.addListener(marker, "click", function() {
      marker.openInfoWindowHtml(html);
      active_gmarker = marker;
    });
    gmarkers.push(marker);
    return marker;
}

// == shows all markers of a particular category, and ensures the checkbox is checked ==
function show(category) {
	var activeMarkers = [];
    for (var i=0; i<gmarkers.length; i++) {
      if (gmarkers[i].mycategory == category) {
        // gmarkers[i].show();
        activeMarkers.push(gmarkers[i]);
      }
    }
    // == check the checkbox ==
    document.getElementById(category+"box").checked = true;
    
    // == marker clusterer
    var markerClusterer = null;
    if (clusterersIcon[category]!=null) {
    	markerClusterer = new MarkerClusterer(map, activeMarkers, {styles: clusterersIcon[category]});
    } else {
    	markerClusterer = new MarkerClusterer(map, activeMarkers);
    }
    clusterers[category] = markerClusterer;
}

// == hides all markers of a particular category, and ensures the checkbox is cleared ==
function hide(category) {
    for (var i=0; i<gmarkers.length; i++) {
      if (gmarkers[i].mycategory == category) {
        gmarkers[i].hide();
      }
    }
    // == clear the checkbox ==
    document.getElementById(category+"box").checked = false;
    // == close the info window, in case its open on a marker that we just hid
    map.closeInfoWindow();
    
    // == marker clusterer
    var markerClusterer = clusterers[category];
    if (markerClusterer!=null && markerClusterer.hasOwnProperty("clearMarkers")) {
    	markerClusterer.clearMarkers();
        markerClusterer = null;
    }
}

// == a checkbox has been clicked ==
function boxclick(box,category) {
    if (box.checked) {
      show(category);
    } else {
      hide(category);
    }
    // == rebuild the side bar
    makeSidebar();
}            

// == This function picks up the click and opens the corresponding info window
function myclick(i) {
	active_gmarker = gmarkers[i];
    GEvent.trigger(gmarkers[i],"click");
}

// == rebuilds the sidebar to match the markers currently displayed ==
function makeSidebar() {
	var html = "<ul class='TTMapMarkerList'>";
	var mem = ""
	var mc = ""
    for (var i=0; i<gmarkers.length; i++) {
      var mc = gmarkers[i].mycategory;
      if((i==0 || mc!=mem) && !gmarkers[i].isHidden()) {
      	html += '<li class="TTMapMarkerListTitle"><b>'+gmarkers[i].mycategoryfullname+'</b></li>';
      }
      mem = mc;
      if (!gmarkers[i].isHidden()) {
        html += '<li class="TTMapMarkerListItem"><a href="javascript:myclick(' + i + ')">' + gmarkers[i].myname + '</a></li>';
      }
    }
    html += "</ul>";
    if(document.getElementById("side_bar")) {
    	document.getElementById("side_bar").innerHTML = html;
    }
}

// == shows a specific marker at map start ==
function showMarkerAtStartup(markerId) {
    var found = false;
    for (var i=0; i<gmarkers.length; i++) {
      if (gmarkers[i].myid == markerId) {
        found=true;

        // activate marker's category
        var category = gmarkers[i].mycategory;
        document.getElementById(category+"box").checked = true;
        show(category);
        makeSidebar();

        //simulate click on marker
        myclick(i);
      }
    }
    if(!found) {
    	errnotify(ERRCODES[TT_NO_MARKER_FOUND]+": "+markerId);
    }
}


// == Create polyline
function createPolyline(position_,defaultActive_,color_,weight_,points_,levels_,zoom_,numLevels_,polylinetxt_) {
    var encodedPolyline = new GPolyline.fromEncoded({
                                color: color_,
                                weight: weight_,
                                points: points_,
                                latlngs: "40,12",
                                levels: levels_,
                                zoomFactor: zoom_,
                                numLevels: numLevels_
                                  });
    
    GEvent.addListener(encodedPolyline, 'click', function(overlay) {
    		map.openInfoWindow(overlay,polylinetxt_);
    });
    
    GEvent.addListener(encodedPolyline, 'mouseover', function(overlay) {
    	// DO NOTHING
    });
    
    if(defaultActive_)
        encodedPolyline.show();
    else
        encodedPolyline.hide();
    gpolylines[position_] = encodedPolyline;
    map.addOverlay(encodedPolyline);
    return encodedPolyline;
}

// == a polyline has been clicked ==
function polylineClick(box,i) {
	var poly = gpolylines[i];
    if (box.checked) {
      poly.show();
      map.setCenter(poly.getBounds().getCenter());
      var midVertex = Math.round(poly.getVertexCount() / 2);
      GEvent.trigger(poly,"click",poly.getVertex(midVertex));
    } else {
    	poly.hide();
    	map.closeInfoWindow();
    }
}

// == Create polygon
function createPolygon(position_,defaultActive_,color_,opacity_,outline_,weight_,points_,levels_,zoom_,numLevels_) {
    var lines = new Array;
    lines.push({
            color:color_,
            weight:weight_,
            opacity:1,
            zoomFactor:zoom_,
            numLevels:numLevels_,
            points:points_,
            levels:levels_
            });

    var encodedPolygon = new GPolygon.fromEncoded({
                            polylines:lines,
                            fill:true,
                            color:color_,
                            opacity:opacity_,
                            outline:outline_
                            });    
    if(defaultActive_)
        map.addOverlay(encodedPolygon);
    gpolygons[position_] = encodedPolygon;    
}

// == a polygon has been clicked ==
function polygonClick(box,i) {
    if (box.checked) {
      map.addOverlay(gpolygons[i]);
      map.setCenter(gpolygons[i].getBounds().getCenter());
    } else {
      map.removeOverlay(gpolygons[i]);
    }
}



// == refresh map position and marker ==
function refreshPosition(point) {
	var map = new GMap2(document.getElementById("map"));
	map.addControl(new GSmallMapControl());
    map.addControl(new GMapTypeControl());
	map.clearOverlays()
    map.setCenter(point,14);
    var marker = new GMarker(point, {
        draggable :true
    });
    map.addOverlay(marker);

    GEvent.addListener(marker, "dragend", function() {
        var pt = marker.getPoint();
        map.panTo(pt);
        document.getElementById(fieldId).value = pt.lat().toFixed(5) + "|" + pt.lng().toFixed(5);
    });

    GEvent.addListener(map, "moveend", function() {
        map.clearOverlays();
        var center = map.getCenter();
        var marker = new GMarker(center, {
            draggable :true
        });
        map.addOverlay(marker);
        document.getElementById(fieldId).value = center.lat().toFixed(5) + "|" + center.lng().toFixed(5);

        GEvent.addListener(marker, "dragend", function() {
            var pt = marker.getPoint();
            map.panTo(pt);
            document.getElementById(fieldId).value = pt.lat().toFixed(5) + "|" + pt.lng().toFixed(5);
        });
    });
}


// == disableCoordinates ==
function disableCoordinates(coordField) {
	document.getElementById(coordField).value = "0|0";
	var lat = 0;
	var long = 0;
	var point = new GLatLng(lat,long);
	refreshPosition(point);
}


// == update latlong (marker edit) ==
function updateMapLatLong(fieldId) {
	var splitCoords= document.getElementById(fieldId).value.split("|");
	var lat = splitCoords[0];
	var long = splitCoords[1];
	var point = new GLatLng(lat,long);
	refreshPosition(point);
}

// == search address (marker edit) ==
function searchAddress(address, fieldId) {
    if (geocoder) {
        geocoder.getLatLng(address, function(point) {
            if (!point) {
            	errnotify(ERRCODES[G_GEO_UNKNOWN_ADDRESS]);
            } else {
            	document.getElementById(fieldId).value = point.lat().toFixed(5) + "|" + point.lng().toFixed(5); 
            	refreshPosition(point);
            }
        });
    }
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


//== Get Directions has been clicked ==//
function get_directions_from_data(){
	var street = document.getElementById("tt_street_address").value;
	var city = document.getElementById("tt_city_name").value;
	var state = document.getElementById("tt_state_name").value;
	var country = document.getElementById("tt_country_name").value;
	var full_address = street + ', ' + city + ', ' + state + ', ' + country;
	if (!geocoder){
        var geocoder = new GClientGeocoder();
	}
	if (active_gmarker==null){
        errnotify(ERRCODES[TT_NO_MARKER_SELECTED]);
	}
	else if (active_directions){
	        active_directions.clear()
	}
	else {
	    active_directions=new GDirections(map, document.getElementById("g_directions"));
	    GEvent.addListener(active_directions, "error", g_notify_error);
	    GEvent.addListener(active_directions, "load", g_clear_on_success);
	}
	
	geocoder.getLatLng(full_address, function(g_point){
	    if (g_point != null) {
	    	try {
	    		active_directions.load("from:" + full_address + "@" + g_point.toUrlValue(6) + " to:" + active_gmarker.myname + "@" + active_gmarker.getLatLng().toUrlValue(6) );
	    		self.location.hash='directionsBox';
	    	} catch (e) {
	    		// do nothing
	    	}	        
	    }
	    else{
	        errnotify(ERRCODES[G_GEO_UNKNOWN_ADDRESS]);
	    }
	});
        
}

//== Notify errors to a section of the page ==
function errnotify(err_message){
	var err_display = document.getElementById('error_display');
	err_display.innerHTML = '<dl class="portalMessage error"><dt>'+ERRCODES[TT_ERROR]+'</dt> <dd>'+err_message+'</dd>  </dl>';
	self.location.hash='errorBox';
}

function g_notify_error(){
	g_directions_status = active_directions.getStatus().code;
	if (g_directions_status != 200){
	    errnotify(ERRCODES[g_directions_status]);
	}
	else{
        errnotify("hellllp");
	}
}

function g_clear_on_success(){
	var err_display = document.getElementById('error_display');
	err_display.innerHTML = "";
}

