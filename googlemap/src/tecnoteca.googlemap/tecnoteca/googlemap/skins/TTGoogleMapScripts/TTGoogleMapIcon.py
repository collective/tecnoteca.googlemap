## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=category, isGlobalMap
##title=

output="var icon;"
if(category.getCustomIcon() != None and category.getCustomIcon() != ""):                
    output+='icon = createIcon(\''+category.absolute_url()+'/CustomIcon'+'\');'
else:
    if(category.getCategoryIcon() != None and category.getCategoryIcon() != ""):
        output+='icon = createIcon(\''+category.getCategoryIcon()+'\');'
    else:
        output+='icon = createIcon(\'ttgooglemap_marker.png\');'
if(isGlobalMap):
    output+='gicons[\''+category.getUniqueId()+'\'] = icon;'
return output