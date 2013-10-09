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
    var icon = new google.maps.MarkerImage(imgUrl);
    
    if(imgsize[0]!=null && imgsize[0]!=0) { // if size defined
        icon.iconSize = new google.maps.Size({width: imgsize[1], height: imgsize[0]}); 
    } else { // set default
        icon.iconSize = new google.maps.Size({width: 32, height: 37});
    }
    icon.iconAnchor = new google.maps.Point(16,34); // set anchor point
    icon.imageMap = [0,0, icon.iconSize.width,0, icon.iconSize.width,icon.iconSize.height, 0,icon.iconSize.height]; // set clickable area
    icon.shadowSize = new google.maps.Size(0, 0); // disable shadow
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
	var marker = new google.maps.Marker({position:point, icon:gicons[category], title:name})	
	
    // === Store the category and name info as a marker properties ===
    marker.myid = id;
    marker.mycategory = category;
    marker.mycategoryfullname = categoryFullName;
    marker.myname = name;
    
    google.maps.event.addListener(marker, "click", function() {
      infoWindow.setContent(html);
      infoWindow.open(map, marker);
      active_gmarker = marker;
    });    
    gmarkers[id]=marker;
    return gmarkers[id];
}

// == shows all markers of a particular category, and ensures the checkbox is checked ==
function show(category) {
	hide(category); // cleanup
	var activeMarkers = [];
    for (var i in gmarkers) {
      if (gmarkers[i].mycategory == category) {
        activeMarkers.push(gmarkers[i]);        
      }
    }

    var markerClusterer = null;
    if (clusterersIcon[category]!=null) {
        markerClusterer = new MarkerClusterer(map, activeMarkers, {styles: clusterersIcon[category]});
    } else {
        markerClusterer = new MarkerClusterer(map, activeMarkers);
    }
    clusterers[category] = markerClusterer;

    
    // == check the checkbox ==
    document.getElementById(category+"box").checked = true;
}

// == hides all markers of a particular category, and ensures the checkbox is cleared ==
function hide(category) {	   
    // == close the info window, in case its open on a marker that we just hid       
    infoWindow.close();

    // == marker clusterer
    var markerClusterer = clusterers[category];
   
    if (markerClusterer!=null) {
        markerClusterer.clearMarkers();
        markerClusterer = null;
    }
    
    // == clear the checkbox ==
    document.getElementById(category+"box").checked = false;   
}

// == a checkbox has been clicked in side box ==
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
function markerclick(i) {
	active_gmarker = gmarkers[i];
	
	// zoom in
	var markerCategory = active_gmarker.mycategory;
	var markerClusterer = clusterers[markerCategory];
	markerClusterer.fitMapToMarkers();
	
	// pan 
	map.panTo(active_gmarker.getPosition());
	
	// trigger click
    google.maps.event.trigger(active_gmarker,"click");
}

// == rebuilds the sidebar to match the markers currently displayed ==
function makeSidebar() {
	var html = "<ul class='TTMapMarkerList'>";
	var mem = ""
	var mc = ""
	for (i in gmarkers) {
      var mc = gmarkers[i].mycategory;
      var catIsChecked = document.getElementById(mc+"box").checked;
      if((i==0 || mc!=mem) && catIsChecked) {
      	html += '<li class="TTMapMarkerListTitle"><b>'+gmarkers[i].mycategoryfullname+'</b></li>';
      }
      mem = mc;
      if (catIsChecked) {
        html += '<li class="TTMapMarkerListItem"><a href="javascript:markerclick(\'' + i + '\')">' + gmarkers[i].myname + '</a></li>';
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
    var i;
    for (i in gmarkers) {
      if (gmarkers[i].myid == markerId) {
        found=true;

        // activate marker's category
        var category = gmarkers[i].mycategory;
        document.getElementById(category+"box").checked = true;
        show(category);
        makeSidebar();        

        //simulate click on marker
        markerclick(i);
      }
    }
    if(!found) {
    	errnotify(ERRCODES['TT_NO_MARKER_FOUND']+": "+markerId);
    }
}


// == Create polyline
function createPolyline(position_,defaultActive_,color_,weight_,points_,levels_,zoom_,numLevels_,polylinetxt_) {
    
    var decodedPath = google.maps.geometry.encoding.decodePath(points_); 
    var decodedLevels = decodeLevels(levels_);
   
   
    var encodedPolyline = new google.maps.Polyline({
        path: decodedPath,
        levels: decodedLevels,
        strokeColor: color_,
        strokeWeight: weight_,
        zoom: zoom_,

    });   
    
    //Polyline Info window
    google.maps.event.addListener(encodedPolyline,'click', function(event){
        var infowindow = new google.maps.InfoWindow({content: polylinetxt_});
        var point = event.latLng;
        var marker = new google.maps.Marker({position:point});
        infowindow.open(map,marker);
    });


    if(defaultActive_)
        encodedPolyline.setMap(map);
    else
        encodedPolyline.setMap(null);    
 
	gpolylines[position_] = encodedPolyline;
}



// == a polyline has been clicked in lateral box ==
function polylineClick(box,i) {
	var poly = gpolylines[i];
	if(poly) {
	    if (box.checked) {
	      gpolylines[i].setMap(map);

	    } else {
	    	gpolylines[i].setMap(null);
	    	infoWindow.close();	    	
	    }
	}
}


// == Create polygon
function createPolygon(html_ , position_,defaultActive_,color_,opacity_,outline_,weight_,points_,levels_,zoom_,numLevels_) {
    var decodedPath = google.maps.geometry.encoding.decodePath(points_); 
    var decodedLevels = decodeLevels(levels_);
   
    if (outline_==false)
    	weight_=0
   
    var polygon = new google.maps.Polygon({
        path: decodedPath,
        fill:true,
        levels: decodedLevels,
        strokeColor: color_,
        strokeOpacity:1,        
        fillColor: color_,
        fillOpacity: opacity_,
        strokeWeight: weight_
    });
    
    google.maps.event.addListener(polygon, 'click', function (event) {
    	var lat = event.latLng.lat();
        var lng = event.latLng.lng();
        var latlng = new google.maps.LatLng(lat, lng);
    	infoWindow.setContent(html_);
    	infoWindow.setPosition(latlng);
        infoWindow.open(map);
    });    
       
    if(defaultActive_)
       polygon.setMap(map);
    gpolygons[position_] = polygon;
}


// == a polygon has been clicked ==
function polygonClick(box,i) {
    if (box.checked) {
      gpolygons[i].setMap(map);

    } else {
      gpolygons[i].setMap(null);	

    }
}


function decodeLevels(encodedLevelsString) {
    var decodedLevels = [];

    for (var i = 0; i < encodedLevelsString.length; ++i) {
        var level = encodedLevelsString.charCodeAt(i) - 63;
        decodedLevels.push(level);
    }
    return decodedLevels;
}


//== Get Directions has been clicked ==//
function get_directions_from_data() {
	var street = document.getElementById("tt_street_address").value;
	var city = document.getElementById("tt_city_name").value;
	var state = document.getElementById("tt_state_name").value;
	var country = document.getElementById("tt_country_name").value;
	var start = street + ', ' + city + ', ' + state + ', ' + country;
	
	if (active_gmarker==null) {
        errnotify(ERRCODES['TT_NO_MARKER_SELECTED']);
	}
	else if (active_directions) {
	    active_directions.clear(); 
	}	
	var latlng = active_gmarker.getPosition();
	
	var geocoder = new google.maps.Geocoder();
	geocoder.geocode({'latLng': latlng}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			if (results[0]) {
				var end = results[0].formatted_address;

				var request = {
					origin : start,
					destination : end,
					travelMode : google.maps.TravelMode.DRIVING
				};
				directionsService.route(request, function(response, status) {
					if (status == google.maps.DirectionsStatus.OK) {
						directionsDisplay.setDirections(response);
					} else {
						errnotify(ERRCODES['G_GEO_UNKNOWN_ADDRESS']);
					}
				});
			}
		} else {
			console.log(results);
			console.log(status);
		}
    });	
}


//== Notify errors to a section of the page ==
function errnotify(err_message) {
	var err_display = document.getElementById('error_display');
	err_display.innerHTML = '<dl class="portalMessage error"><dt>'+ERRCODES['TT_ERROR']+'</dt> <dd>'+err_message+'</dd>  </dl>';
	self.location.hash='errorBox';
}

//== Notify errors to a popup ==
function errpopup(err_message) {
	alert(ERRCODES['TT_ERROR'] + ": " + err_message);
}


function addMapButton(HTMLlabel, callbackFunction) {
	
	  var buttonDiv = document.createElement('div');
	  buttonDiv.index = 1;

	  buttonDiv.style.padding = '5px';

	  // Set CSS for the control border
	  var controlUI = document.createElement('div');
	  controlUI.style.backgroundColor = 'white';
	  controlUI.style.borderStyle = 'solid';
	  controlUI.style.borderWidth = '1px';
	  controlUI.style.borderColor = '#717B87';	  
	  controlUI.style.cursor = 'pointer';
	  controlUI.style.textAlign = 'center';
	  buttonDiv.appendChild(controlUI);

	  // Set CSS for the control interior
	  var controlText = document.createElement('div');
	  controlText.style.paddingLeft = '6px';
	  controlText.style.paddingRight = '6px';
	  controlText.style.paddingTop = '1px';
	  controlText.style.paddingBottom = '1px';
	  controlText.innerHTML = HTMLlabel;
	  controlUI.appendChild(controlText);

	  google.maps.event.addDomListener(controlUI, 'click', function() {
		  callbackFunction();
	  });
	  
	  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(buttonDiv);

	}

