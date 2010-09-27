## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=categories
##title=

newline="\n"
output=""
for catloop in categories:
    category = catloop.getObject()
    
    # default active
    if(category.getDefaultActive()):
        output+="show(\""+category.UID()+"\");";
    else:
        output+="hide(\""+category.UID()+"\");";
        
    output += newline
        
return output