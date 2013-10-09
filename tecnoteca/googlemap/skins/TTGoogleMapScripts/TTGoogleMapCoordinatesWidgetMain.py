## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=marker,default_location,coordFieldId
##title=

from tecnoteca.googlemap import googlemapMessageFactory as _

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

var ERRCODES = new Array(); 
ERRCODES['TT_ERROR'] = " """ + context.translate(_(u'TT_ERROR')) + """ ";
ERRCODES['G_GEO_UNKNOWN_ADDRESS'] =" """ + context.translate(_(u'G_GEO_UNKNOWN_ADDRESS')) + """ ";


coordFieldId = '"""+ (coordFieldId!=None and str(coordFieldId) or '') +"""';

editMode = false;
if(coordFieldId)
    editMode = true;

Gload = function() {
    var initialPosition = new google.maps.LatLng("""+str(latitude)+""", """+str(longitude)+""");    

    // map
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: initialPosition,        
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        draggable: editMode,
        panControl: editMode,
    });
    google.maps.event.addListener(map, "dragend", function() {
        refreshMarkerPosition(map.getCenter());
    });
    
    
    // marker
    marker = new google.maps.Marker({
        draggable: editMode
    });
    marker.setMap(map);
    google.maps.event.addListener(marker, "dragend", function() {
        refreshMarkerPosition(marker.position);
    });
    refreshMarkerPosition(initialPosition);
}
   
   google.maps.event.addDomListener(window, 'load', Gload);
   
</script>
"""

return output