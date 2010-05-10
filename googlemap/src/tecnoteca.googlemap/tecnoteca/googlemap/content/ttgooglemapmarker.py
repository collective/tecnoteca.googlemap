"""Definition of the TTGoogleMapMarker content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMapMarker
from tecnoteca.googlemap.config import PROJECTNAME

TTGoogleMapMarkerSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    
    atapi.TextField(
        'Text',
        storage=atapi.AnnotationStorage(),
        default_output_type= 'text/x-html-safe',
        widget=atapi.RichWidget(
            label=_(u"Text"),
            description=_(u"Marker text"),
        ),
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
    
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TTGoogleMapMarkerSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapMarkerSchema['description'].storage = atapi.AnnotationStorage()
TTGoogleMapMarkerSchema['description'].widget.visible = {'view':'hidden','edit':'hidden'}

schemata.finalizeATCTSchema(TTGoogleMapMarkerSchema, moveDiscussion=False)


class TTGoogleMapMarker(base.ATCTContent):
    """Google Map Marker"""
    implements(ITTGoogleMapMarker)

    meta_type = "TTGoogleMapMarker"
    schema = TTGoogleMapMarkerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    Text = atapi.ATFieldProperty('Text')
    
    Coordinates = atapi.ATFieldProperty('Coordinates')
    
    def getUniqueId(self):
        return ( self.getId() + str(self.created().millis()) )
    
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

atapi.registerType(TTGoogleMapMarker, PROJECTNAME)
