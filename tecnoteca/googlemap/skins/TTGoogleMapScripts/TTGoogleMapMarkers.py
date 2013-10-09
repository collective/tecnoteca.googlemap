## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=categories
##title=

helper = context.restrictedTraverse('@@ttgooglemap_helpersview')     

output=""

## loop through categories
for catloop in categories:
    category = catloop.getObject()
    markers = category.getMarkers()
    
    # loop through markers
    for entry in markers:
        marker = entry.getObject()
        
        if not(hasattr(marker, "getLatitude")) or marker.getLatitude() == None or marker.isDisabled():
            continue        
            
        # info window html
        html = helper.getTitleHTML(marker)
        html += helper.getDescriptionHTML(marker)
        html += helper.getRelatedItemsHTML(marker);
            
        latlng = "new google.maps.LatLng("+marker.getLatitude()+","+marker.getLongitude()+")"
            
        # create marker
        output += "\n"
        output += "mgr.addMarker(createMarker("
        output += "\"" + marker.UID() + "\""
        output += ","
        output += latlng
        output += ","
        output += "\"" + helper.customEscape(marker.Title()) + "\""
        output += ","
        output += "\"" + html + "\""
        output += ","
        output += "\"" + category.UID() + "\""
        output += ","
        output += "\"" + helper.customEscape(category.pretty_title_or_id()) + "\""
        output += "));"
        
return output