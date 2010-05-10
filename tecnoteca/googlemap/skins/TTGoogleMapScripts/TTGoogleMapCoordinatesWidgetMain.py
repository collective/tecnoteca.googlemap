## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=marker,default_location,coordFieldId
##title=

# edit-mode js
edit_mode_listeners = """
GEvent.addListener(marker, "dragend", function() {
    var point = marker.getPoint();
    map.panTo(point);
    document.getElementById(fieldId).value = point.lat().toFixed(5) + "|" + point.lng().toFixed(5);
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
        var point = marker.getPoint();
        map.panTo(point);
        document.getElementById(fieldId).value = point.lat().toFixed(5) + "|" + point.lng().toFixed(5);
    });

});
"""

# init lat/long
latitude = marker.getLatitude()
if( latitude==None or latitude=="" ):
    latitude = default_location[0]
longitude = marker.getLongitude()
if( longitude==None or longitude=="" ):
    longitude = default_location[1]


# create main
output = """
<script type="text/javascript">

var fieldId = '"""+ (coordFieldId!=None and str(coordFieldId) or '') +"""';

Gload = function() {
     if (GBrowserIsCompatible()) {
         var map = new GMap2(document.getElementById("map"));
         map.addControl(new GSmallMapControl());
         map.addControl(new GMapTypeControl());
         var center = new GLatLng("""+str(latitude)+""", """+str(longitude)+""");
         map.setCenter(center, 15);
         geocoder = new GClientGeocoder();
         var marker = new GMarker(center, {draggable: true});
         map.addOverlay(marker);
         
         """+ (coordFieldId!=None and edit_mode_listeners or '') +"""
     }
   }
   
   // register functions
   registerEventListener(window, 'load', Gload);
   registerEventListener(window, 'unload', GUnload);
   
</script>
"""

return output