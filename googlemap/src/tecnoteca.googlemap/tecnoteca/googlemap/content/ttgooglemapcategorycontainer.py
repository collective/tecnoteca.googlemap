"""Definition of the TTGoogleMapCategoryContainer content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMapCategoryContainer
from tecnoteca.googlemap.config import PROJECTNAME

TTGoogleMapCategoryContainerSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

TTGoogleMapCategoryContainerSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapCategoryContainerSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    TTGoogleMapCategoryContainerSchema,
    folderish=True,
    moveDiscussion=False
)


class TTGoogleMapCategoryContainer(folder.ATFolder):
    """Group of categories"""
    implements(ITTGoogleMapCategoryContainer)

    meta_type = "TTGoogleMapCategoryContainer"
    schema = TTGoogleMapCategoryContainerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(TTGoogleMapCategoryContainer, PROJECTNAME)
