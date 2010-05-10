from zope import schema
from zope.interface import Interface

from tecnoteca.googlemap import googlemapMessageFactory as _


class ITTGoogleMapPolyline(Interface):
    """Google Map Polyline"""

    # -*- schema definition goes here -*-
    Color = schema.TextLine(
        title=_(u"Color"),
        required=True,
        description=_(u"Polyline color"),
    )
#
    DefaultActive = schema.Bool(
        title=_(u"Default Active"),
        required=False,
        description=_(u"Default active"),
    )
#
    Weight = schema.Int(
        title=_(u"Weight"),
        required=True,
        description=_(u"Line thickness (px)"),
    )
#
    EncodedPolyline = schema.TextLine(
        title=_(u"Encoded Polyline"),
        required=True,
        description=_(u"Encoded polyline"),
    )
#
    Levels = schema.TextLine(
        title=_(u"Levels"),
        required=True,
        description=_(u"Encoded levels"),
    )
#
    ZoomFactor = schema.Int(
        title=_(u"Zoom Factor"),
        required=True,
        description=_(u"Zoom factor"),
    )
#
    NumLevels = schema.Int(
        title=_(u"Num Levels"),
        required=True,
        description=_(u"Number of levels"),
    )
#
