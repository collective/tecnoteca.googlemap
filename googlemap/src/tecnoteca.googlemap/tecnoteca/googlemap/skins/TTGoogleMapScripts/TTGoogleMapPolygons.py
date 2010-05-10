## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=polygons
##title=

output=""
count=0;
for polyloop in polygons:    
    polygon = polyloop.getObject()
    count = count+1
    
    output += "createPolygon("
    output += str(count)
    output += ","
    output += str(polygon.getDefaultActive()).lower()
    output += ","
    output += "\""+str(polygon.getColor())+"\""
    output += ","
    output += str(polygon.getOpacity())
    output += ","
    output += str(polygon.getOutline()).lower()
    output += ","
    output += str(polygon.getWeight())
    output += ","
    output += "\""+str(polygon.getEncodedPolyline())+"\""
    output += ","
    output += "\""+str(polygon.getLevels())+"\""
    output += ","
    output += str(polygon.getZoomFactor())
    output += ","
    output += str(polygon.getNumLevels())
    output += ");";
    output += "\n";
    
return output