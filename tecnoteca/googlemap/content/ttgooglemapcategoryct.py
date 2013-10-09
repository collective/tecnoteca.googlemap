"""Definition of the TTGoogleMapCategoryCT content type
"""

from zope.interface import implements
from zope.component import getMultiAdapter

from time import time
from plone.memoize import ram

from Products.CMFCore.utils import getToolByName

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMapCategoryCT
from tecnoteca.googlemap.config import *
from tecnoteca.googlemap.content.ttgooglemapcategory import TTGoogleMapCategorySchema,TTGoogleMapCategory, markers_cachekey
from tecnoteca.googlemap.browser.logger import log

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
    
    @property
    def gmap_category_objecttype(self):
        return self.getCType()
    
    @ram.cache(markers_cachekey)
    def getMarkers(self, **args):
        log('Query the catalog to get markers for TTGoogleMapCategoryCT. Content Type: "%s"' % self.getCType())
        catalog = getToolByName(self, 'portal_catalog')
        return catalog(portal_type = self.getCType(), review_state = "published", **args)
    
    def configuredContentTypes(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.get_configured_content_types()

base.registerATCT(TTGoogleMapCategoryCT, PROJECTNAME)
