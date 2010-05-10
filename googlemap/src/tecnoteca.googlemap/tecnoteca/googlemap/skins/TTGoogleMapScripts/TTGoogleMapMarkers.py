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
        text = text.replace("\r\n", "")
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
    markers = category.getFolderContents(contentFilter={'portal_type':'TTGoogleMapMarker', 'review_state':'published'});
    
    # loop through markers
    for markloop in markers:
        marker = markloop.getObject()
        
        output += newline;
        output += newline;
        
        # lat - lng
        output += "point = new GLatLng("+marker.getLatitude()+","+marker.getLongitude()+");"
        output += newline;
        
        # title and text 
        output += "html = '<div class=\"TTMapMarkerWin\">';"
        output += newline 
        output += "html += \"<b>"+custom_escape(marker.Title())+"</b><br>"+(custom_escape(marker.getText())).strip()+"\";"
        output += newline;
        
        # relations                            
        output += "html += '<ul>';"
        output += newline
        for relation in marker.getRelatedItems(): # standard relation (marker >> object)
            output += "html += '<li>';"
            output += "html += \"<a href='"+relation.absolute_url()+"' title='"+custom_escape(relation.Title())+"'>"+custom_escape(relation.Title())+"</a>\";"
            output += "html += '</li>';"
            output += newline
        for relation in marker.getBRefs(): # custom relation (object >> marker)
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
        output += "map.addOverlay(createMarker(\""+marker.getUniqueId()+"\", point, \""+custom_escape(marker.Title())+"\", html, '"+category.getUniqueId()+"'));"
        
return output