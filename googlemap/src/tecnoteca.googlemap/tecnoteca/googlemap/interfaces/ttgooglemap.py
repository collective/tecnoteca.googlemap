from zope import schema
from zope.interface import Interface

from tecnoteca.googlemap import googlemapMessageFactory as _


class ITTGoogleMap(Interface):
    """Google Map Object"""

    # -*- schema definition goes here -*-
    Text = schema.Text(
        title=_(u"Text"),
        required=False,
        description=_(u"Text on top of the map"),
    )
#
    MapWidth = schema.Int(
        title=_(u"Map Width"),
        required=True,
        description=_(u"Map width (px)"),
    )
#
    MapHeight = schema.Int(
        title=_(u"Map Height"),
        required=True,
        description=_(u"Map height (px)"),
    )
#
    ZoomLevel = schema.Int(
        title=_(u"Zoom Level"),
        required=True,
        description=_(u"Default zoom level"),
    )
#
    MapType = schema.TextLine(
        title=_(u"Map Type"),
        required=True,
        description=_(u"Select default map type"),
    )
#    
    CatBoxHeight = schema.Int(
        title=_(u"Cat Box Height"),
        required=True,
        description=_(u"Cat box max-height"),
    )
#   
    MarkerBoxHeight = schema.Int(
        title=_(u"Marker Box Height"),
        required=True,
        description=_(u"Marker box max-height"),
    )
#
    Panoramio = schema.Bool(
        title=_(u"Panoramio"),
        required=False,
        description=_(u"Show Panoramio button"),
    )
#
    LargeMapControl = schema.Bool(
        title=_(u"Large Map Control"),
        required=False,
        description=_(u"Large map control buttons"),
    )
#
    MapTypeControl = schema.Bool(
        title=_(u"Map Type Control"),
        required=False,
        description=_(u"Show map type buttons"),
    )
#
    OverviewMapControl = schema.Bool(
        title=_(u"Overview Map Control"),
        required=False,
        description=_(u"Show the overview map"),
    )
#
