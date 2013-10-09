"""Definition of the TTGoogleMapCategory content type
"""

from zope.interface import implements
from zope.component import getMultiAdapter

from time import time
from plone.memoize import ram
from Products.CMFCore.interfaces._content import ISiteRoot

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from Products.CMFCore.utils import getToolByName

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMap
from tecnoteca.googlemap.interfaces import ITTGoogleMapCategory
from tecnoteca.googlemap.config import *
from tecnoteca.googlemap.browser.config import TTGoogleMapConfig
from tecnoteca.googlemap.browser.logger import log

TTGoogleMapCategorySchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-    
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
        default='cluster3.png',
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

    
    atapi.ImageField(
        'ClustererIcon',
        storage=atapi.AnnotationStorage(),
        widget=atapi.ImageWidget(
            label=_(u"Clusterer icon"),
            description=_(u"Select a custom icon for clusterer"),
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

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

TTGoogleMapCategorySchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapCategorySchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    TTGoogleMapCategorySchema,
    folderish=True,
    moveDiscussion=False
)


def markers_cachekey(method, self, **args):
    """
    Returns the key used by @ram.cache
    """
    # get ram cache seconds property
    ptool = getToolByName(self, 'portal_properties')
    sheet = getToolByName(ptool, PROPERTY_SHEET)
    ram_cache_seconds = sheet.getProperty(PROPERTY_MARKERS_CACHE, 1)
    # if ram_cache_seconds is 0 sets it to 0.001 for division 
    if not ram_cache_seconds:
        ram_cache_seconds = 0.001
    # set the key for context
    the_key = list(self.getPhysicalPath())
    the_key.append(time() // ram_cache_seconds)
    return the_key

class TTGoogleMapCategory(folder.ATFolder):
    """Google Map Category"""
    implements(ITTGoogleMapCategory)

    meta_type = "TTGoogleMapCategory"
    schema = TTGoogleMapCategorySchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    CustomIcon = atapi.ATFieldProperty('CustomIcon')
    
    ClustererIcon = atapi.ATFieldProperty('ClustererIcon')

    CategoryIcon = atapi.ATFieldProperty('CategoryIcon')

    DefaultActive = atapi.ATFieldProperty('DefaultActive')
    
    def markerIconVocab(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.marker_icons
    
    def getParentMap(self, context = None):
        if not context:
            context = self.aq_inner
        if ITTGoogleMap.providedBy(context):
            return context
        elif ISiteRoot.providedBy(context):
            return None
        else:
            return self.getParentMap(context.aq_parent)
    
    @ram.cache(markers_cachekey)
    def getMarkers(self, **args):
        log('Query the catalog to get markers for TTGoogleMapCategory. Category: "%s"' % self.Title())
        filter={'portal_type':'TTGoogleMapMarker', 'review_state':'published'}
        if args:
            filter = dict(filter.items() + args.items())            
        return self.getFolderContents(contentFilter=filter);

base.registerATCT(TTGoogleMapCategory, PROJECTNAME)
