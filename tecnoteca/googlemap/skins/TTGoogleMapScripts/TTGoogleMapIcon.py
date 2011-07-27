## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=category, isGlobalMap
##title=

newline="\n"
output=""
if(category.getCustomIcon() != None and category.getCustomIcon() != ""):                
    output+='icon = createIcon(\''+category.absolute_url()+'/CustomIcon'+'\');'
else:
    if(category.getCategoryIcon() != None and category.getCategoryIcon() != ""):
        output+='icon = createIcon(\''+category.getCategoryIcon()+'\');'
    else:
        output+='icon = createIcon(\'ttgooglemap_marker.png\');'

if(category.getClustererIcon() != None and category.getClustererIcon() != ""):
    output+='clustererIcon = createClustererIcon(\''+category.absolute_url()+'/ClustererIcon'+'\');'
else:
    output+='clustererIcon = null;'

output += newline

if(isGlobalMap):
    output+='gicons[\''+category.UID()+'\'] = icon;'
    output+='clusterersIcon[\''+category.UID()+'\'] = clustererIcon;'
    output += newline
    
return output