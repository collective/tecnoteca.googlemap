from zope import schema
from zope.interface import Interface

from tecnoteca.googlemap import googlemapMessageFactory as _


class ITTGoogleMapPolygon(Interface):
    """Google Map Polygon"""

    # -*- schema definition goes here -*-
    Color = schema.TextLine(
        title=_(u"Color"),
        required=True,
        description=_(u"Polygon color"),
    )
#
    Opacity = schema.Float(
        title=_(u"Opacity"),
        required=True,
        description=_(u"Opacity level"),
    )
#
    Outline = schema.Bool(
        title=_(u"Outline"),
        required=False,
        description=_(u"Outline area"),
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
        description=_(u"Zoom Factor"),
    )
#
    NumLevels = schema.Int(
        title=_(u"Num Levels"),
        required=True,
        description=_(u"Number of levels"),
    )
#
