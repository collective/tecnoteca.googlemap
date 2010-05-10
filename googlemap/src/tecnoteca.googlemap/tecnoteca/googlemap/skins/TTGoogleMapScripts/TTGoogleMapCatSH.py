## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=categories
##title=

output=""
for catloop in categories:
    category = catloop.getObject()
    
    # default active
    if(category.getDefaultActive()):
        output+="show(\""+category.getUniqueId()+"\");";
    else:
        output+="hide(\""+category.getUniqueId()+"\");";    
        
return output