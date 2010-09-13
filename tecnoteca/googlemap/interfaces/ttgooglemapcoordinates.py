from zope import schema
from zope.interface import Interface

from tecnoteca.googlemap import googlemapMessageFactory as _


class ITTGoogleMapCoordinates(Interface):
    """Google Map Marker"""

    # -*- schema definition goes here -*-
    Coordinates = schema.TextLine(
        title=_(u"Coordinates"),
        required=True,
        description=_(u"Coordinates lat long"),
    )