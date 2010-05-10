## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=polylines
##title=

output=""
count=0;
for polyloop in polylines:    
    polyline = polyloop.getObject()
    count = count+1
    
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
    output += ");";
    output += "\n";
    
return output