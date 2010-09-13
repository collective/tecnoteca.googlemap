from zope import schema
from zope.interface import Interface

from tecnoteca.googlemap import googlemapMessageFactory as _

class ITTGoogleMapCategoryCT(Interface):
    """Google Map Category Content Type"""

    # -*- schema definition goes here -*-
    CType = schema.TextLine(
        title=_(u"Content type"),
        required=True,
        description=_(u"Select content type"),
    )
#
    CustomIcon = schema.Bytes(
        title=_(u"Custom icon"),
        required=False,
        description=_(u"Select a custom icon for category"),
    )
#
    CategoryIcon = schema.TextLine(
        title=_(u"CategoryIcon"),
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