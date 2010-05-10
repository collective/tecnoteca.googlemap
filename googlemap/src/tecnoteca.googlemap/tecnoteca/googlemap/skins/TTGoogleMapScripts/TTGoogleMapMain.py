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
if(defaultMarker!=None and defaultMarker!=""):
    defaultMarker = 'showMarkerAtStartup(\''+str(defaultMarker)+'\');'
else:
    defaultMarker = ''

# main js
output = """
<script type="text/javascript">
//<![CDATA[

// init vars
var gmarkers = [];
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