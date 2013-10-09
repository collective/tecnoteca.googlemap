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

# panoramio js code
jsPano = "var panoramioLayer = new google.maps.panoramio.PanoramioLayer();" 
jsPano += "panoramioLayer.setMap(map);"
jsPano += "addMapButton('%s', function() {panoramioLayer.setMap(panoramioLayer.getMap() ? null : map);} );" % context.translate(_(u"Panoramio"))

# weather js code
jsWeather = "var weatherLayer = new google.maps.weather.WeatherLayer();" 
jsWeather += "weatherLayer.setMap(map);"
jsWeather += "addMapButton('%s', function() {weatherLayer.setMap(weatherLayer.getMap() ? null : map);} );" % context.translate(_(u"Weather"))

# traffic js code
jsTraffic = "var trafficLayer = new google.maps.TrafficLayer();" 
jsTraffic += "trafficLayer.setMap(map);"
jsTraffic += "addMapButton('%s', function() {trafficLayer.setMap(trafficLayer.getMap() ? null : map);} );" % context.translate(_(u"Traffic"))

# bicycle js code
jsBicycle = "var bicycleLayer = new google.maps.BicyclingLayer();" 
jsBicycle += "bicycleLayer.setMap(map);"
jsBicycle += "addMapButton('%s', function() {bicycleLayer.setMap(bicycleLayer.getMap() ? null : map);} );" % context.translate(_(u"Bicycle"))

# directions js code
jsDirections = "directionsService = new google.maps.DirectionsService();"
jsDirections += "directionsDisplay = new google.maps.DirectionsRenderer();"
jsDirections += "directionsDisplay.setMap(map);"
jsDirections += "directionsDisplay.setPanel(document.getElementById('g_directions'));"

# main js
output = """
<script type="text/javascript">
//<![CDATA[

var ERRCODES = new Array(); 
ERRCODES['TT_ERROR'] = " """ + context.translate(_(u'TT_ERROR')) + """ ";
ERRCODES['G_GEO_SUCCESS'] = " """ + context.translate(_(u'G_GEO_SUCCESS')) + """ ";
ERRCODES['G_GEO_BAD_REQUEST'] = " """ + context.translate(_(u'G_GEO_BAD_REQUEST')) + """ ";
ERRCODES['G_GEO_SERVER_ERROR'] =" """ + context.translate(_(u'G_GEO_SERVER_ERROR')) + """ ";
ERRCODES['G_GEO_MISSING_QUERY'] =" """ + context.translate(_(u'G_GEO_MISSING_QUERY')) + """ ";
ERRCODES['G_GEO_MISSING_ADDRESS'] =" """ + context.translate(_(u'G_GEO_MISSING_ADDRESS')) +""" ";
ERRCODES['G_GEO_UNKNOWN_ADDRESS'] =" """ + context.translate(_(u'G_GEO_UNKNOWN_ADDRESS')) + """ ";
ERRCODES['G_GEO_UNAVAILABLE_ADDRESS'] = " """ + context.translate(_(u'G_GEO_UNAVAILABLE_ADDRESS')) +""" ";
ERRCODES['G_GEO_UNKNOWN_DIRECTIONS'] = " """ + context.translate(_(u'G_GEO_UNKNOWN_DIRECTIONS')) +""" ";
ERRCODES['G_GEO_BAD_KEY'] = " """ + context.translate(_(u'G_GEO_BAD_KEY')) + """ ";
ERRCODES['G_GEO_TOO_MANY_QUERIES'] = " """ + context.translate(_(u'G_GEO_TOO_MANY_QUERIES')) + """ ";
ERRCODES['TT_NO_MARKER_SELECTED'] = " """ + context.translate(_(u'TT_NO_MARKER_SELECTED')) + """ ";
ERRCODES['TT_NO_MARKER_FOUND'] = " """ + context.translate(_(u'TT_NO_MARKER_FOUND')) + """ ";

// init vars
var icon;
var overview_control="""+test(googleMap.getOverviewMapControl()==True,'true','false')+""";
var maptype_control="""+test(googleMap.getMapTypeControl()==True,'true','false')+""";
var streetview_control="""+test(googleMap.getStreetViewControl()==True,'true','false')+""";
var gmarkers = new Object();
var clusterers = new Array();
var clusterersIcon = new Array();
var active_gmarker = null;
var active_directions = null;
var gicons = [];
var gpolylines = [];
var gpolygons = [];
var htmls = [];
var i = 0;
var mgr;
var map;
var infoWindow;
var mc;

//var activeMarkers = []

        
Gload = function() {

    // create the map
    map = new google.maps.Map(
        document.getElementById('map'), {   
            center: new google.maps.LatLng("""+str(googleMap.getLatitude())+""", """+str(googleMap.getLongitude())+"""), 
            mapTypeId: """+ googleMap.getMapType() +""",
            zoom : """+str(googleMap.getZoomLevel())+""",
            overviewMapControl: overview_control,
            overviewMapControlOptions: {opened: true},
            mapTypeControl: maptype_control,
            streetViewControl: streetview_control
      });
    
     //var activeMarkers = []

    // map directions
    """+ (googleMap.getDirections() and jsDirections or "") +"""
    
    // map controls
    """+ (googleMap.getPanoramio() and jsPano or "") +"""
    """+ (googleMap.getWeather() and jsWeather or "") +"""
    """+ (googleMap.getTraffic() and jsTraffic or "") +"""
    """+ (googleMap.getBicycle() and jsBicycle or "") +"""
    
    // marker manager
    mgr = new MarkerManager(map);
    
    
    // info window
    infoWindow = new google.maps.InfoWindow();
    
    google.maps.event.addListener(mgr, 'loaded', function() { 
    
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

    });

}

google.maps.event.addDomListener(window, 'load', Gload);


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