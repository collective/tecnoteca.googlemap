"""Definition of the TTGoogleMap content type
"""

from zope.interface import implements
from zope.component import getMultiAdapter

from Products.Archetypes import atapi
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMap
from tecnoteca.googlemap.config import PROJECTNAME

TTGoogleMapSchema = folder.ATFolderSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.TextField(
        'Text',
        storage=atapi.AnnotationStorage(),
        default_output_type= 'text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Text"),
            description=_(u"Text on top of the map"),
        ),
    ),


    atapi.IntegerField(
        'MapWidth',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.IntegerWidget(
            label=_(u"Map Width"),
            description=_(u"Map width (px)"),
        ),
        required=True,
        default_method = 'defaultWidth',
        validators=('isInt'),
    ),


    atapi.IntegerField(
        'MapHeight',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.IntegerWidget(
            label=_(u"Map Height"),
            description=_(u"Map height (px)"),
        ),
        required=True,
        default_method = 'defaultHeight',
        validators=('isInt'),
    ),


    atapi.TextField(
        'Coordinates',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Coordinates"),
            description=_(u"Coordinates lat long"),
            macro='TTGoogleMapCoordinatesWidget',
        ),
        required=True,
    ),


    atapi.IntegerField(
        'ZoomLevel',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.IntegerWidget(
            label=_(u"Zoom Level"),
            description=_(u"Default zoom level"),
        ),
        required=True,
        default=13,
        validators=('isInt'),
    ),


    atapi.StringField(
        'MapType',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        vocabulary = [("G_NORMAL_MAP","Normal"),("G_SATELLITE_MAP","Satellite"),("G_HYBRID_MAP","Hybrid")],
        widget=atapi.SelectionWidget(
            label=_(u"Map Type"),
            description=_(u"Select default map type"),
        ),
        default="G_NORMAL_MAP",
        required=True,
    ),


    atapi.BooleanField(
        'Panoramio',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Panoramio"),
            description=_(u"Show Panoramio button"),
        ),
        default=True,
    ),


    atapi.BooleanField(
        'LargeMapControl',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Large Map Control"),
            description=_(u"Large map control buttons"),
        ),
        default=True,
    ),


    atapi.BooleanField(
        'MapTypeControl',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Map Type Control"),
            description=_(u"Show map type buttons"),
        ),
        default=True,
    ),


    atapi.BooleanField(
        'OverviewMapControl',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Overview Map Control"),
            description=_(u"Show the overview map"),
        ),
        default=True,
    ),
    
    atapi.BooleanField(
        'OpenBoxes',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"OpenBoxes"),
            description=_(u"Open boxes"),
        ),
        default=True,
    ),

))

# Set storage on fields copied from ATFolderSchema, making sure
# they work well with the python bridge properties.

TTGoogleMapSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(
    TTGoogleMapSchema,
    folderish=True,
    moveDiscussion=False
)


class TTGoogleMap(folder.ATFolder):
    """Google Map Object"""
    implements(ITTGoogleMap)

    meta_type = "TTGoogleMap"
    schema = TTGoogleMapSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    Text = atapi.ATFieldProperty('Text')

    MapWidth = atapi.ATFieldProperty('MapWidth')

    MapHeight = atapi.ATFieldProperty('MapHeight')

    Coordinates = atapi.ATFieldProperty('Coordinates')

    ZoomLevel = atapi.ATFieldProperty('ZoomLevel')

    MapType = atapi.ATFieldProperty('MapType')

    Panoramio = atapi.ATFieldProperty('Panoramio')

    LargeMapControl = atapi.ATFieldProperty('LargeMapControl')

    MapTypeControl = atapi.ATFieldProperty('MapTypeControl')

    OverviewMapControl = atapi.ATFieldProperty('OverviewMapControl')
    
    StartupBoxes = atapi.ATFieldProperty('OpenBoxes')
    
    def getLatitude(self):
        coordinates = self.getCoordinates().split("|")
        if(len(coordinates)>1):
            return coordinates[0]
        else:
            return None
    
    def getLongitude(self):
        coordinates = self.getCoordinates().split("|")
        if(len(coordinates)>1):
            return coordinates[1]
        else:
            return None
    
    def defaultWidth(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.default_map_size[1]
    
    def defaultHeight(self):
        config = getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
        return config.default_map_size[0]

atapi.registerType(TTGoogleMap, PROJECTNAME)
