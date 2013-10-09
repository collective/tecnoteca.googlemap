"""Definition of the TTGoogleMapMarker content type
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
from tecnoteca.googlemap.interfaces import ITTGoogleMapMarker
from tecnoteca.googlemap.config import PROJECTNAME
from tecnoteca.googlemap.content.ttgooglemapcoordinates import *

TTGoogleMapMarkerSchema = schemata.ATContentTypeSchema.copy() + TTGoogleMapCoordinatesSchema.copy() + atapi.Schema((

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
    
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TTGoogleMapMarkerSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapMarkerSchema['description'].storage = atapi.AnnotationStorage()
TTGoogleMapMarkerSchema['description'].widget.visible = {'view':'hidden','edit':'hidden'}

schemata.finalizeATCTSchema(TTGoogleMapMarkerSchema, moveDiscussion=False)


class TTGoogleMapMarker(base.ATCTContent, TTGoogleMapCoordinates):
    """Google Map Marker"""
    implements(ITTGoogleMapMarker)

    meta_type = "TTGoogleMapMarker"
    schema = TTGoogleMapMarkerSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    Text = atapi.ATFieldProperty('Text')    

base.registerATCT(TTGoogleMapMarker, PROJECTNAME)
