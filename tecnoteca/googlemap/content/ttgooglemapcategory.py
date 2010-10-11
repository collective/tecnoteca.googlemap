"""Definition of the TTGoogleMapCategory content type
"""

from zope.interface import implements
from zope.component import getMultiAdapter

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata
from Products.CMFCore.utils import getToolByName

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMapCategory
from tecnoteca.googlemap.config import PROJECTNAME
from tecnoteca.googlemap.browser.config import TTGoogleMapConfig

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


class TTGoogleMapCategory(folder.ATFolder):
    """Google Map Category"""
    implements(ITTGoogleMapCategory)

    meta_type = "TTGoogleMapCategory"
    schema = TTGoogleMapCategorySchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    CustomIcon = atapi.ATFieldProperty('CustomIcon')

    CategoryIcon = atapi.ATFieldProperty('CategoryIcon')

    DefaultActive = atapi.ATFieldProperty('DefaultActive')
    
    def markerIconVocab(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.marker_icons
    
    def getMarkers(self, **args):
        filter={'portal_type':'TTGoogleMapMarker', 'review_state':'published'}
        if args:
            filter = dict(filter.items() + args.items())            
        return self.getFolderContents(contentFilter=filter);

atapi.registerType(TTGoogleMapCategory, PROJECTNAME)
