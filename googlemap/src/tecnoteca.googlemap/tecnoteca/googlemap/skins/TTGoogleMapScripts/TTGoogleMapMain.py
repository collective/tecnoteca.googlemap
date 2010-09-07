## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=googleMap,categories,contentFilterCategories,catcontainers,polylines,polygons
##title=


# generate categories' icon
mapCatIcons = googleMap.TTGoogleMapCatIcons(categories)
mapCatIcons += googleMap.TTGoogleMapCatContainers(catcontainers,contentFilterCategories,'icons')

# generate categories' show/hide
mapCatSH = googleMap.TTGoogleMapCatSH(categories)
mapCatSH += googleMap.TTGoogleMapCatContainers(catcontainers,contentFilterCategories,'showhide')

# generate markers' code
mapMarkers = googleMap.TTGoogleMapMarkers(categories)
mapMarkers += googleMap.TTGoogleMapCatContainers(catcontainers,contentFilterCategories,'markers')

# generate polylines' code
mapPolyjs = googleMap.TTGoogleMapPolylines(polylines)

# generate polygons' code
mapPolygjs = googleMap.TTGoogleMapPolygons(polygons)

# get default marker (if any)
defaultMarker = context.REQUEST.get("mk");
if defaultMarker is None:
    defaultMarker = googleMap.getDefaultMarker()
if(defaultMarker!=None and defaultMarker!=""):
    defaultMarker = 'showMarkerAtStartup(\''+str(defaultMarker)+'\');'
else:
    defaultMarker = ''

# main js
output = """
<script type="text/javascript">
//<![CDATA[
var ERRCODES = new Array(); 
var TT_NO_MARKER_SELECTED = 667;
ERRCODES[G_GEO_SUCCESS] = " """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_success", default="No errors occurred; the address was successfully parsed and its geocode has been returned." ) + """ ";
ERRCODES[G_GEO_BAD_REQUEST] = " """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_bad_request", default="A directions request could not be successfully parsed. For example, the request may have been rejected if it contained more than the maximum number of waypoints allowed.") + """ ";
ERRCODES[G_GEO_SERVER_ERROR] =" """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_server_error", default="A geocoding, directions or maximum zoom level request could not be successfully processed, yet the exact reason for the failure is not known.") + """ ";
ERRCODES[G_GEO_MISSING_QUERY] =" """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_missing_query", default="The HTTP q parameter was either missing or had no value. For geocoding requests, this means that an empty address was specified as input. For directions requests, this means that no query was specified in the input") + """ ";
ERRCODES[G_GEO_MISSING_ADDRESS] =" """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_missing_address", default="The HTTP q parameter was either missing or had no value. For geocoding requests, this means that an empty address was specified as input. For directions requests, this means that no query was specified in the input") +""" ";
ERRCODES[G_GEO_UNKNOWN_ADDRESS] =" """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_unknown_address", default="No corresponding geographic location could be found for the specified address. This may be due to the fact that the address is relatively new, or it may be incorrect.")+ """ ";
ERRCODES[G_GEO_UNAVAILABLE_ADDRESS] = " """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_unanailable_address", default="The geocode for the given address or the route for the given directions query cannot be returned due to legal or contractual reasons.") +""" ";
ERRCODES[G_GEO_UNKNOWN_DIRECTIONS] = " """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_unknown_directions", default="The GDirections object could not compute directions between the points mentioned in the query. This is usually because there is no route available between the two points, or because we do not have data for routing in that region.") +""" ";
ERRCODES[G_GEO_BAD_KEY] = " """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_bad_key", default="The given key is either invalid or does not match the domain for which it was given.") + """ ";
ERRCODES[G_GEO_TOO_MANY_QUERIES] = " """ + context.translate(domain="tecnoteca.googlemap" ,msgid="g_geo_too_may_queries", default="The given key has gone over the requests limit in the 24 hour period or has submitted too many requests in too short a period of time. If you re sending multiple requests in parallel or in a tight loop, use a timer or pause in your code to make sure you dont send the requests too quickly.")+ """ ";
ERRCODES[TT_NO_MARKER_SELECTED] = " """ + context.translate(domain="tecnoteca.googlemap" ,msgid="tt_no_marker_selected", default="You must select the destination marker before, if none is available please add one or contact your site administrator to do so." ) + """ ";

// init vars
var gmarkers = [];
var active_gmarker = null;
var active_directions = null;
var gicons = [];
var gpolylines = [];      
var gpolygons = [];
var htmls = [];
var i = 0;
var map;
        
Gload = function() {
    if (GBrowserIsCompatible()) {
        
        
        // create the map
        map = new GMap2(document.getElementById("map"));
        
        // set center
        var center = new GLatLng("""+str(googleMap.getLatitude())+""", """+str(googleMap.getLongitude())+"""); 
        map.setCenter(center, """+str(googleMap.getZoomLevel())+""");    
        
        // map controls
        map.setMapType("""+ googleMap.getMapType() +""");    
        """+ (googleMap.getLargeMapControl() and "map.addControl(new GLargeMapControl());" or "map.addControl(new GSmallMapControl());") +"""
        """+ (googleMap.getMapTypeControl() and "map.addControl(new GMapTypeControl());" or "") +"""
        """+ (googleMap.getOverviewMapControl() and "map.addControl(new GOverviewMapControl());" or "") +"""
        """+ (googleMap.getPanoramio() and "map.addControl(new PanoMapTypeControl()); var geocoder = new GClientGeocoder();" or "") +"""                        
        
        // icons
        """+mapCatIcons+"""
        
        // markers
        """+mapMarkers+"""
        
        // categories show/hide
        """+mapCatSH+"""
        
        //polylines
        """+mapPolyjs+"""
    
        //polygons
        """+mapPolygjs+"""
        
        // create the initial sidebar    
        makeSidebar();
        
        // default marker js
        """+defaultMarker+"""
    }
}

// register functions
registerEventListener(window, 'load', Gload);
registerEventListener(window, 'unload', GUnload);

// initialize jquery panels
jq(document).ready(function() {
    // hide or show the all of the element with class TTMapCollapsiblePanelContent
    """+ (googleMap.getOpenBoxes() and "jq(\".TTMapCollapsiblePanelContent\").show();" or "jq(\".TTMapCollapsiblePanelContent\").hide();") +"""
    // toggle the componenet with class TTMapCollapsiblePanelContent
    jq(".TTMapCollapsiblePanelTab").click(function(){
        jq(this).next(".TTMapCollapsiblePanelContent").slideToggle(250);
        jq(this).children(".TTMapPanelOpenClose").toggle();
    });
});

//]]>
</script>
"""

return output

