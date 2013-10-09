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
        if not props_sheet.hasProperty(property['id']):
            props_sheet.manage_addProperty(id = property['id'], value = property['value'], type = property['type'])           

def updateIndexes(portal):
    catalog_tool = getToolByName(portal, 'portal_catalog')
    if 'gmap_category_objecttype' not in catalog_tool.indexes():
        catalog_tool.addIndex(name = 'gmap_category_objecttype',
                              type = 'FieldIndex')
def setupVarious(context):

    if context.readDataFile('tecnoteca.googlemap_various.txt') is None:
        return
    
    # Add additional setup code here
    portal = context.getSite()
    # update prop
    updateProperties(portal)
    updateIndexes(portal)