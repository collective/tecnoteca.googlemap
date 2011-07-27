## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=categories
##title=

def custom_escape(text):
        text = text.replace('"','\\"')
        text = text.replace('“','&quot;')
        text = text.replace('”','&quot;')
        text = text.replace("\r", "")
        text = text.replace("\n", "")
        text = unicode(text, errors='ignore')
        return text     

newline="\n"
output=""

# create js vars
output += "var point;"
output += newline
output += "var html;"
output += newline

## loop through categories
for catloop in categories:
    category = catloop.getObject()
    markers = category.getMarkers()
    
    # loop through markers
    for entry in markers:
        marker = entry.getObject()
        
        if not(hasattr(marker, "getLatitude")) or marker.getLatitude() == None or marker.isDisabled():
            continue
        
        output += newline;
        output += newline;
        
        # lat - lng
        output += "point = new GLatLng("+marker.getLatitude()+","+marker.getLongitude()+");"
        output += newline;
        
        # title and description 
        output += "html = '<div class=\"TTMapMarkerWin\">';"
        output += newline 
        if marker.portal_type == 'TTGoogleMapMarker': # if TTGoogleMapMarker object
            output += "html += \"<b>"+custom_escape(marker.Title())+"</b><br/>"+(custom_escape(marker.getText())).strip()+"\";"
        else: # content-type obj
            output += "html += \"<a href='"+marker.absolute_url()+"'><b>"+custom_escape(marker.Title())+"</b></a><br/>"
            output += (custom_escape(marker.Description())).strip()+"\";"
        output += newline;
        
        # relations
        if marker.getRelatedItems() or marker.getBRefs():
            output += "html += '<ul>';"
            output += newline
            for relation in marker.getRelatedItems(): # standard relation (marker >> object)
                if relation and relation.getLanguage()==context.REQUEST.get("Language","it"):
                    output += "html += '<li>';"
                    output += "html += \"<a href='"+relation.absolute_url()+"' title='"+custom_escape(relation.Title())+"'>"+custom_escape(relation.Title())+"</a>\";"
                    output += "html += '</li>';"
                    output += newline
            for relation in marker.getBRefs(): # custom relation (object >> marker)
                if relation and relation.getLanguage()==context.REQUEST.get("Language","it"):
                    output += "html += '<li>';"
                    output += "html += \"<a href='"+relation.absolute_url()+"' title='"+custom_escape(relation.pretty_title_or_id())+"'>"+custom_escape(relation.pretty_title_or_id())+"</a>\";"
                    output += "html += '</li>';"
                    output += newline
            output += "html += '</ul>';"
            output += newline
            
        output += "html += '<br/>';"
        output += newline
        output += "html += '</div>';"
            
        # careate marker
        output += newline
        output += "map.addOverlay(createMarker(\""+marker.UID()+"\", point, \""+custom_escape(marker.Title())+"\", html, '"+category.UID()+"', \""+custom_escape(category.pretty_title_or_id())+"\"));"
        
return output