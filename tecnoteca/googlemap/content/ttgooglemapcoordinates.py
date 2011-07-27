"""Definition of the TTGoogleMapCoordinates content type
"""

from zope.interface import implements

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMapCoordinates

TTGoogleMapCoordinatesSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
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

TTGoogleMapCoordinatesSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapCoordinatesSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TTGoogleMapCoordinatesSchema, moveDiscussion=False)

class TTGoogleMapCoordinates(base.ATCTContent):
    """Google Map Coordinates"""
    implements(ITTGoogleMapCoordinates)

    meta_type = "TTGoogleMapCoordinates"
    schema = TTGoogleMapCoordinatesSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    Coordinates = atapi.ATFieldProperty('Coordinates')
    
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
    
    def isDisabled(self):
        return (self.getLatitude()=="0" and self.getLongitude()=="0")
