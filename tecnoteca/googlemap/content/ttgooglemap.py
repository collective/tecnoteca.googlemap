"""Definition of the TTGoogleMap content type
"""

from zope.interface import implements
from zope.component import getMultiAdapter

from Products.CMFCore.utils import getToolByName

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMap
from tecnoteca.googlemap.config import PROJECTNAME
from tecnoteca.googlemap.content.ttgooglemapcoordinates import *

TTGoogleMapSchema = folder.ATFolderSchema.copy() + TTGoogleMapCoordinatesSchema.copy() + atapi.Schema((

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
    ),
    
                                                                                                       
    atapi.BooleanField(
        'FullWidth',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"FullWidth"),
            description=_(u"Set map to full width (overrides MapWidth)"),
        ),
        default=True,
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
    ),


    atapi.StringField(
        'MapType',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        vocabulary = [("google.maps.MapTypeId.ROADMAP","Normal"),
                      ("google.maps.MapTypeId.SATELLITE","Satellite"),
                      ("google.maps.MapTypeId.HYBRID","Hybrid"),
                      ("google.maps.MapTypeId.TERRAIN","Terrain")],
        widget=atapi.SelectionWidget(
            label=_(u"Map Type"),
            description=_(u"Select default map type"),
        ),
        default="google.maps.MapTypeId.ROADMAP",
        required=True,
    ),
    
    
    atapi.IntegerField(
        'CatBoxHeight',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.IntegerWidget(
            label=_(u"Cat Box Height"),
            description=_(u"Cat box max-height"),
        ),
        required=True,
        default_method = 'defaultCatBoxHeight',
    ),
    
    
    atapi.IntegerField(
        'MarkerBoxHeight',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.IntegerWidget(
            label=_(u"Marker Box Height"),
            description=_(u"Marker box max-height"),
        ),
        required=True,
        default_method = 'defaultMarkerBoxHeight',
    ),
    
    

    atapi.BooleanField(
        'Panoramio',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Panoramio"),
            description=_(u"Show Panoramio button"),
        ),
        default=False,
    ),
                                                                                                       
                                                                                                       
                                                                                                       
    atapi.BooleanField(
        'Weather',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Weather"),
            description=_(u"Show weather button"),
        ),
        default=False,
    ),
                                                                                                       
                                                                                                       
                                                                                                       
    atapi.BooleanField(
        'Traffic',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Traffic"),
            description=_(u"Show traffic button"),
        ),
        default=False,
    ),  
                                                                                                       
                                                                                                       
                                                                                                       
    atapi.BooleanField(
        'Bicycle',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Bicycle"),
            description=_(u"Show bicycle button"),
        ),
        default=False,
    ),  
                                                                                                       


    atapi.BooleanField(
        'StreetViewControl',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Street View Control"),
            description=_(u"Street view map control button"),
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
    
    atapi.BooleanField(
        'Directions',
        storage=atapi.AnnotationStorage(),
        languageIndependent = True,
        widget=atapi.BooleanWidget(
            label=_(u"Directions"),
            description=_(u"Show directions"),
        ),
        default=True,
    ),    
    
    atapi.StringField(
        'DefaultMarker',
        storage=atapi.AnnotationStorage(),
        default_output_type= 'text/x-html-safe',
        widget=atapi.SelectionWidget (
            format="select",
            label=_(u"Default Marker"),
            description=_(u"Default marker startup"),
        ),
        vocabulary="getMarkersVocabulary",
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


class TTGoogleMap(folder.ATFolder, TTGoogleMapCoordinates):
    """Google Map Object"""
    implements(ITTGoogleMap)

    meta_type = "TTGoogleMap"
    schema = TTGoogleMapSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')    

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    Text = atapi.ATFieldProperty('Text')

    MapWidth = atapi.ATFieldProperty('MapWidth')
    
    FullWidth = atapi.ATFieldProperty('FullWidth')

    MapHeight = atapi.ATFieldProperty('MapHeight')

    ZoomLevel = atapi.ATFieldProperty('ZoomLevel')

    MapType = atapi.ATFieldProperty('MapType')
    
    CatBoxHeight = atapi.ATFieldProperty('CatBoxHeight')
    
    MarkerBoxHeight = atapi.ATFieldProperty('MarkerBoxHeight')

    Panoramio = atapi.ATFieldProperty('Panoramio')
    
    Weather = atapi.ATFieldProperty('Weather')
    
    Traffic = atapi.ATFieldProperty('Traffic')
    
    Bicycle = atapi.ATFieldProperty('Bicycle')    

    StreetViewControl = atapi.ATFieldProperty('StreetViewControl')

    MapTypeControl = atapi.ATFieldProperty('MapTypeControl')

    OverviewMapControl = atapi.ATFieldProperty('OverviewMapControl')
    
    OpenBoxes = atapi.ATFieldProperty('OpenBoxes')
    
    Directions = atapi.ATFieldProperty('Directions')
    
    DefaultMarker = atapi.ATFieldProperty('DefaultMarker')
    
    def getConfig(self):
        return getMultiAdapter((self, self.REQUEST), name="ttgooglemap_config")
    
    def defaultWidth(self):
        return self.getConfig().default_map_size[1]
    
    def defaultHeight(self):
        return self.getConfig().default_map_size[0]
    
    def defaultCatBoxHeight(self):
        mapHeight = int(self.defaultHeight())
        return (mapHeight * 35 / 100) # 35% total map height
    
    def defaultMarkerBoxHeight(self):
        mapHeight = int(self.defaultHeight())
        return (mapHeight * 55 / 100) # 55% total map height
    
    def getMarkersVocabulary(self):
        vocabulary = atapi.DisplayList()
        vocabulary.add('','-')

        for cat in self.getFolderContents(contentFilter={'portal_type':('TTGoogleMapCategory','TTGoogleMapCategoryCT'),'path':{'depth':3, 'query':'/'.join(self.getPhysicalPath()) }}):
            category = cat.getObject()
            markers = category.getMarkers()
            for item in markers:
                marker = item.getObject()
                if not marker.isDisabled():
                    vocabulary.add( str(item.UID), item.pretty_title_or_id())
        
        return vocabulary

base.registerATCT(TTGoogleMap, PROJECTNAME)