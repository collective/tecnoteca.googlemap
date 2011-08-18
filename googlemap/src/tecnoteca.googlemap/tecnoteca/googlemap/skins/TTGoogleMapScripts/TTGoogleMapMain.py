## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=googleMap,categories,contentFilterCategories,catcontainers,polylines,polygons,defaultMarker
##title=

from tecnoteca.googlemap import googlemapMessageFactory as _

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

# default marker (if any)
mapDefaultMarker = ''
if(defaultMarker!=None and defaultMarker!=""):
    mapDefaultMarker = 'showMarkerAtStartup(\''+str(defaultMarker)+'\');'


# main js
output = """
<script type="text/javascript">
//<![CDATA[
var ERRCODES = new Array(); 
var TT_NO_MARKER_SELECTED = 667;
var TT_NO_MARKER_FOUND = 668;
var TT_ERROR = 669;

ERRCODES[TT_ERROR] = " """ + context.translate(_(u'TT_ERROR')) + """ ";
ERRCODES[G_GEO_SUCCESS] = " """ + context.translate(_(u'G_GEO_SUCCESS')) + """ ";
ERRCODES[G_GEO_BAD_REQUEST] = " """ + context.translate(_(u'G_GEO_BAD_REQUEST')) + """ ";
ERRCODES[G_GEO_SERVER_ERROR] =" """ + context.translate(_(u'G_GEO_SERVER_ERROR')) + """ ";
ERRCODES[G_GEO_MISSING_QUERY] =" """ + context.translate(_(u'G_GEO_MISSING_QUERY')) + """ ";
ERRCODES[G_GEO_MISSING_ADDRESS] =" """ + context.translate(_(u'G_GEO_MISSING_ADDRESS')) +""" ";
ERRCODES[G_GEO_UNKNOWN_ADDRESS] =" """ + context.translate(_(u'G_GEO_UNKNOWN_ADDRESS')) + """ ";
ERRCODES[G_GEO_UNAVAILABLE_ADDRESS] = " """ + context.translate(_(u'G_GEO_UNAVAILABLE_ADDRESS')) +""" ";
ERRCODES[G_GEO_UNKNOWN_DIRECTIONS] = " """ + context.translate(_(u'G_GEO_UNKNOWN_DIRECTIONS')) +""" ";
ERRCODES[G_GEO_BAD_KEY] = " """ + context.translate(_(u'G_GEO_BAD_KEY')) + """ ";
ERRCODES[G_GEO_TOO_MANY_QUERIES] = " """ + context.translate(_(u'G_GEO_TOO_MANY_QUERIES')) + """ ";
ERRCODES[TT_NO_MARKER_SELECTED] = " """ + context.translate(_(u'TT_NO_MARKER_SELECTED')) + """ ";
ERRCODES[TT_NO_MARKER_FOUND] = " """ + context.translate(_(u'TT_NO_MARKER_FOUND')) + """ ";

// init vars
var icon;
var gmarkers = [];
var clusterers = new Array();
var clusterersIcon = new Array();
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
        """+ (googleMap.getMapTypeControl() and "// map.addControl(new GMapTypeControl());" or "") +"""
        """+ (googleMap.getOverviewMapControl() and "map.addControl(new GOverviewMapControl());" or "") +"""
        """+ (googleMap.getPanoramio() and "map.addControl(new PanoMapTypeControl()); var geocoder = new GClientGeocoder();" or "") +"""                        
        
        // icons
        """+mapCatIcons+"""
        
        // polylines
        """+mapPolyjs+"""
    
        // polygons
        """+mapPolygjs+"""
        
        // markers
        """+mapMarkers+"""
        
        // categories show/hide
        """+mapCatSH+"""                
        
        // create the initial sidebar    
        makeSidebar();
        
        // default marker js
        """+mapDefaultMarker+"""
                
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