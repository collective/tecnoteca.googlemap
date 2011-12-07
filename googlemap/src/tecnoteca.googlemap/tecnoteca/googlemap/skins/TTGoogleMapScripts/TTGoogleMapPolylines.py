## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=polylines
##title=

def custom_escape(text):
        text = text.replace('"','\\"')
        text = text.replace('“','&quot;')
        text = text.replace('”','&quot;')
        text = text.replace("\r", "")
        text = text.replace("\n", "")
        text = unicode(text, errors='ignore')
        return text   

mtool = getattr(context,'portal_membership')
isAnonymousUser = mtool.isAnonymousUser()

newline="\n"
output="var polylinetxt;"
output += newline

count=0;
for polyloop in polylines:    
    polyline = polyloop.getObject()
    count = count+1
    
    output += "polylinetxt = \"<a href='"+polyline.absolute_url()+"'><b>"+custom_escape(polyline.Title())+"</b></a><br/>"
    output += (custom_escape(polyline.Description())).strip()+"\";"
    output += newline
    
    # relations
    if polyline.getRelatedItems() or polyline.getBRefs():
        output += "polylinetxt += '<ul>';"
        output += newline
        for relation in polyline.getRelatedItems(): # standard relation (polyline >> object)
            if relation and relation.getLanguage()==context.REQUEST.get("Language","it"):
                output += "polylinetxt += '<li>';"
                output += "polylinetxt += \"<a href='"+relation.absolute_url()+"' title='"+custom_escape(relation.Title())+"'>"+custom_escape(relation.Title())+"</a>\";"
                output += "polylinetxt += '</li>';"
                output += newline
        for relation in polyline.getBRefs(): # custom relation (object >> polyline)
            if relation and relation.getLanguage()==context.REQUEST.get("Language","it"):
                output += "polylinetxt += '<li>';"
                output += "polylinetxt += \"<a href='"+relation.absolute_url()+"' title='"+custom_escape(relation.pretty_title_or_id())+"'>"+custom_escape(relation.pretty_title_or_id())+"</a>\";"
                output += "polylinetxt += '</li>';"
                output += newline
        output += "polylinetxt += '</ul>';"
        output += newline
    
    output += "createPolyline("
    output += str(count)
    output += ","
    output += str(polyline.getDefaultActive()).lower()
    output += ","
    output += "\""+str(polyline.getColor())+"\""
    output += ","
    output += str(polyline.getWeight())
    output += ","
    output += "\""+str(polyline.getEncodedPolyline())+"\""
    output += ","
    output += "\""+str(polyline.getLevels())+"\""
    output += ","
    output += str(polyline.getZoomFactor())
    output += ","
    output += str(polyline.getNumLevels())
    output += ","
    output += "polylinetxt"
    output += ","
    output += str(isAnonymousUser)
    output += ");";
    output += "\n";
    
return output
