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
    
    atapi.StringField(
        'CategoryIcon',
        storage=atapi.AnnotationStorage(),
        vocabulary="markerIconVocab",
        widget=atapi.SelectionWidget(
            label=_(u"Icon"),
            description=_(u"Category icon"),
            macro='TTGoogleMapIconWidget',
        ),
        required=True,
    ),
    

    atapi.ImageField(
        'CustomIcon',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Custom icon"),
            description=_(u"Select a custom icon for category"),
        ),
        validators=('isNonEmptyFile'),
    ),


    atapi.BooleanField(
        'DefaultActive',
        storage=atapi.AnnotationStorage(),
        widget=atapi.BooleanWidget(
            label=_(u"Default Active"),
            description=_(u"Default active at map start"),
        ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TTGoogleMapCategoryCTSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapCategoryCTSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TTGoogleMapCategoryCTSchema, moveDiscussion=False)


class TTGoogleMapCategoryCT(base.ATCTContent):
    """Google Map Category Content Type"""
    implements(ITTGoogleMapCategoryCT)

    meta_type = "TTGoogleMapCategoryCT"
    schema = TTGoogleMapCategoryCTSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    CustomIcon = atapi.ATFieldProperty('CustomIcon')
    CategoryIcon = atapi.ATFieldProperty('CategoryIcon')
    DefaultActive = atapi.ATFieldProperty('DefaultActive')
    CType = atapi.ATFieldProperty('CType')
    
    def markerIconVocab(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.marker_icons
    
    def getMarkers(self):
        catalog = getToolByName(self, 'portal_catalog')
        return catalog(portal_type = self.getCType())
    
    def configuredContentTypes(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.get_configured_content_types()

atapi.registerType(TTGoogleMapCategoryCT, PROJECTNAME)
