## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=catcontainers,contentFilterCategories,section
##title=

output=""
for catcontloop in catcontainers:
    catcontainer = catcontloop.getObject() 
    subcategories = catcontainer.getFolderContents(contentFilter=contentFilterCategories);
    for catloop in subcategories:
        if(section=='icons'):
            output += context.TTGoogleMapCatIcons([catloop])
        elif(section=='showhide'):
            output += context.TTGoogleMapCatSH([catloop])
        elif(section=='markers'):
            output += context.TTGoogleMapMarkers([catloop])
return output