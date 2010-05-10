## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=categories
##title=looping foldercontents (master map)

output=""
for catloop in categories:
    category = catloop.getObject()
    output+=context.TTGoogleMapIcon(category, True)
return output