from zope import schema

from tecnoteca.googlemap import googlemapMessageFactory as _
from tecnoteca.googlemap.interfaces.ttgooglemapcategory import ITTGoogleMapCategory

class ITTGoogleMapCategoryCT(ITTGoogleMapCategory):
    """Google Map Category Content Type"""

    # -*- schema definition goes here -*-
    CType = schema.TextLine(
        title=_(u"Content type"),
        required=True,
        description=_(u"Select content type"),
    )
#