## Script (Python) ""
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=

parentNode = context.getParentNode()
while (parentNode!= None and parentNode.portal_type != "TTGoogleMap"):
    parentNode = parentNode.getParentNode()
      
return parentNode