from Products.CMFCore.utils import getToolByName
from tecnoteca.googlemap.config import *
import transaction

PRODUCT_DEPENDENCIES = ('SmartColorWidget',)

EXTENSION_PROFILES = ('tecnoteca.googlemap:default',)
        
# updates properties sheet
def updateProperties(portal):
    props_tool = getToolByName(portal, 'portal_properties')
    # check if the property sheet exists. if not, create a new one
    if not hasattr(props_tool, PROPERTY_SHEET):
        props_tool.addPropertySheet(id = PROPERTY_SHEET, title=PROPERTY_SHEET_TITLE)
    # get the property sheet
    props_sheet = getToolByName(props_tool, PROPERTY_SHEET)
    # add properties to the sheet
    for property in PROPERTIES_LIST:
        print property
        if not props_sheet.hasProperty(property['id']):
            props_sheet.manage_addProperty(id = property['id'], value = property['value'], type = property['type'])           

def setupVarious(context):
    # Add additional setup code here
    portal = context.getSite()
    # update prop
    updateProperties(portal)