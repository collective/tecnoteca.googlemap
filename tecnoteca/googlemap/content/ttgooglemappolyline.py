"""Definition of the TTGoogleMapPolyline content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces import ITTGoogleMapPolyline
from tecnoteca.googlemap.config import PROJECTNAME

from Products.SmartColorWidget.Widget import SmartColorWidget

TTGoogleMapPolylineSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'Color',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=SmartColorWidget(
            label=_(u"Color"),
            description=_(u"Polyline color"),
        ),
        required=True,
        default="#00CCFF",
    ),


    atapi.BooleanField(
        'DefaultActive',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.BooleanWidget(
            label=_(u"Default Active"),
            description=_(u"Default active at map start"),
        ),
        default=False,
    ),


    atapi.IntegerField(
        'Weight',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Weight"),
            description=_(u"Line thickness (px)"),
        ),
        required=True,
        default=10,
        validators=('isInt'),
    ),


    atapi.StringField(
        'EncodedPolyline',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Encoded Polyline"),
            description=_(u"Encoded polyline value"),
        ),
        required=True,
    ),


    atapi.StringField(
        'Levels',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Levels"),
            description=_(u"Encoded levels"),
        ),
        required=True,
    ),


    atapi.IntegerField(
        'ZoomFactor',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Zoom Factor"),
            description=_(u"Zoom factor parameter"),
        ),
        required=True,
        default=32,
        validators=('isInt'),
    ),


    atapi.IntegerField(
        'NumLevels',
        languageIndependent = True,
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Num Levels"),
            description=_(u"Number of levels"),
        ),
        required=True,
        default=4,
        validators=('isInt'),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

TTGoogleMapPolylineSchema['title'].storage = atapi.AnnotationStorage()
TTGoogleMapPolylineSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(TTGoogleMapPolylineSchema, moveDiscussion=False)


class TTGoogleMapPolyline(base.ATCTContent):
    """Google Map Polyline"""
    implements(ITTGoogleMapPolyline)

    meta_type = "TTGoogleMapPolyline"
    schema = TTGoogleMapPolylineSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    Color = atapi.ATFieldProperty('Color')

    DefaultActive = atapi.ATFieldProperty('DefaultActive')

    Weight = atapi.ATFieldProperty('Weight')

    EncodedPolyline = atapi.ATFieldProperty('EncodedPolyline')

    Levels = atapi.ATFieldProperty('Levels')

    ZoomFactor = atapi.ATFieldProperty('ZoomFactor')

    NumLevels = atapi.ATFieldProperty('NumLevels')


atapi.registerType(TTGoogleMapPolyline, PROJECTNAME)
