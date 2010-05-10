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
    icon.shadowSize = new GSize(0, 0); // disable shadow
    return icon;
}      

// == Create marker ==
function createMarker(id,point,name,html,category) {
    var marker = new GMarker(point,gicons[category]);
    // === Store the category and name info as a marker properties ===
    marker.myid = id;
    marker.mycategory = category;
    marker.myname = name;
    GEvent.addListener(marker, "click", function() {
      marker.openInfoWindowHtml(html);
    });
    gmarkers.push(marker);
    return marker;
}

// == shows all markers of a particular category, and ensures the checkbox is checked ==
function show(category) {
    for (var i=0; i<gmarkers.length; i++) {
      if (gmarkers[i].mycategory == category) {
        gmarkers[i].show();
      }
    }
    // == check the checkbox ==
    document.getElementById(category+"box").checked = true;
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
    GEvent.trigger(gmarkers[i],"click");
}

// == rebuilds the sidebar to match the markers currently displayed ==
function makeSidebar() {
	var html = "<table border='0'>";
    for (var i=0; i<gmarkers.length; i++) {
      if (!gmarkers[i].isHidden()) {
        html += '<tr><td>&bull; </td><td><a href="javascript:myclick(' + i + ')">' + gmarkers[i].myname + '</a></td></tr>';
      }
    }
    html += "</table>";
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
        alert("No marker found with id "+markerId);
    }
}


// == Create polyline
function createPolyline(position_,defaultActive_,color_,weight_,points_,levels_,zoom_,numLevels_) {
    var encodedPolyline = new GPolyline.fromEncoded({
                                color: color_,
                                weight: weight_,
                                points: points_,
                                levels: levels_,
                                zoomFactor: zoom_,
                                numLevels: numLevels_
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
    if (box.checked) {
      gpolylines[i].show();
    } else {
      gpolylines[i].hide();
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
    } else {
      map.removeOverlay(gpolygons[i]);
    }
}

// == search address (marker edit) ==
function searchAddress(address, fieldId) {
    var map = new GMap2(document.getElementById("map"));
    map.addControl(new GSmallMapControl());
    map.addControl(new GMapTypeControl());
    if (geocoder) {
        geocoder.getLatLng(address, function(point) {
            if (!point) {
                alert(address + " not found");
            } else {
            	document.getElementById(fieldId).value = point.lat().toFixed(5) + "|" + point.lng().toFixed(5); 
                map.clearOverlays()
                map.setCenter(point, 14);
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