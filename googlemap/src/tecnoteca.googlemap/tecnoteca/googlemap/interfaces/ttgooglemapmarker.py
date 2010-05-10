from zope import schema
from zope.interface import Interface

from tecnoteca.googlemap import googlemapMessageFactory as _


class ITTGoogleMapMarker(Interface):
    """Google Map Marker"""

    # -*- schema definition goes here -*-
    Text = schema.Text(
        title=_(u"Text"),
        required=False,
        description=_(u"Marker text"),
    )    
    
    Coordinates = schema.TextLine(
        title=_(u"Coordinates"),
        required=True,
        description=_(u"Coordinates lat long"),
    )