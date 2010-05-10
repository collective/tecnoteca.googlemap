from zope import schema
from zope.interface import Interface

from tecnoteca.googlemap import googlemapMessageFactory as _


class ITTGoogleMapCategory(Interface):
    """Google Map Category"""

    # -*- schema definition goes here -*-
    CustomIcon = schema.Bytes(
        title=_(u"Custom icon"),
        required=False,
        description=_(u"Select a custom icon for category"),
    )
#
    Icon = schema.TextLine(
        title=_(u"Icon"),
        required=False,
        description=_(u"Category icon"),
    )
#
    DefaultActive = schema.Bool(
        title=_(u"Default Active"),
        required=False,
        description=_(u"Category selected (active) at map start"),
    )
#
