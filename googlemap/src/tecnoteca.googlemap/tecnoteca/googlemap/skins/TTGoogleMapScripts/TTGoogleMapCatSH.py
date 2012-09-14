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

cats_to_show = context.REQUEST.get('showcats', '').split('|')

for catloop in categories:
    category = catloop.getObject()
    
    # default active
    if(category.getDefaultActive() or category.UID() in cats_to_show):
        output+="show(\""+category.UID()+"\");";
    else:
        output+="hide(\""+category.UID()+"\");";
        
    output += newline
        
return output