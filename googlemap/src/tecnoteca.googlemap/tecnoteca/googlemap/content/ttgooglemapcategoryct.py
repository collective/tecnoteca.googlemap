"""Definition of the TTGoogleMapCategoryCT content type
"""

from zope.interface import implements
from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMapCategoryCT
from tecnoteca.googlemap.config import PROJECTNAME
from tecnoteca.googlemap.content.ttgooglemapcategory import TTGoogleMapCategorySchema,TTGoogleMapCategory

TTGoogleMapCategoryCTSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*- 
    atapi.StringField(
        'CType',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        vocabulary="configuredContentTypes",
        widget=atapi.SelectionWidget(
            label=_(u"Content type"),
            description=_(u"Select content type"),
        ),
        required=True,
    ),
)) + TTGoogleMapCategorySchema.copy()

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.
TTGoogleMapCategoryCTSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapCategoryCTSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TTGoogleMapCategoryCTSchema, moveDiscussion=False)


class TTGoogleMapCategoryCT(TTGoogleMapCategory):
    """Google Map Category Content Type"""
    implements(ITTGoogleMapCategoryCT)

    meta_type = "TTGoogleMapCategoryCT"
    schema = TTGoogleMapCategoryCTSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    CType = atapi.ATFieldProperty('CType')
    
    def getMarkers(self, **args):
        catalog = getToolByName(self, 'portal_catalog')
        return catalog(portal_type = self.getCType(), review_state = "published", **args)
    
    def configuredContentTypes(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.get_configured_content_types()

atapi.registerType(TTGoogleMapCategoryCT, PROJECTNAME)
