from zope.interface import Interface
from zope.component import adapts
from zope.interface import implements
from zope.formlib.form import FormFields

from zope.i18nmessageid import MessageFactory

from zope.schema import Tuple
from zope.schema import TextLine

from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from plone.app.controlpanel.form import ControlPanelForm

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot

from tecnoteca.googlemap.config import *


_ = MessageFactory('tecnoteca.googlemap')


class IMapsSchema(Interface):
    
    googlemaps_keys = Tuple(
        title=_(u'GoogleMap api keys'),
        description=_(u"GoogleMap api keys desc"),
        required=True,
        missing_value=tuple(),
        value_type=TextLine())
            
    default_location = TextLine(
        title=_(u'Default location'),
        description=_(u"Default location desc"),
        required=True)
    
    default_mapsize = TextLine(
        title=_(u'Default mapsize'),
        description=_(u"Default mapsize desc"),
        required=True)
    
    widget_mapsize = TextLine(
        title=_(u'Coordinates widget mapsize'),
        description=_(u"Coordinates widget mapsize desc"),
        required=True)
    
    marker_icons = Tuple(
        title=_(u'Available icons'),
        description=_(u"Available icons desc"),
        missing_value=tuple(),
        required=True,
        value_type=TextLine())


class MapsControlPanelAdapter(SchemaAdapterBase):

    adapts(IPloneSiteRoot)
    implements(IMapsSchema)

    def __init__(self, context):
        super(MapsControlPanelAdapter, self).__init__(context)
        properties = getToolByName(context, 'portal_properties')
        self.context = properties.ttgooglemap_properties



    def get_googlemaps_keys(self):
        return getattr(self.context, PROPERTY_GOOGLE_KEYS, '')

    def set_googlemaps_keys(self, value):
        self.context._updateProperty(PROPERTY_GOOGLE_KEYS, value)

    googlemaps_keys = property(get_googlemaps_keys, set_googlemaps_keys)



    def get_default_location(self):
        return getattr(self.context,PROPERTY_DEFAULT_LOCATION,"46.10262,13.20933")

    def set_default_location(self, value):
        self.context._updateProperty(PROPERTY_DEFAULT_LOCATION, value)

    default_location = property(get_default_location,set_default_location)
    
    
    
    def get_default_mapsize(self):
        return getattr(self.context,PROPERTY_DEFAULT_MAPSIZE,"400,550")

    def set_default_mapsize(self, value):
        self.context._updateProperty(PROPERTY_DEFAULT_MAPSIZE, value)

    default_mapsize = property(get_default_mapsize,set_default_mapsize)

    

    def get_widget_mapsize(self):
        return getattr(self.context,PROPERTY_COORD_WIDGET_MAP_SIZE,"400,400")

    def set_widget_mapsize(self, value):
        self.context._updateProperty(PROPERTY_COORD_WIDGET_MAP_SIZE, value)

    widget_mapsize = property(get_widget_mapsize,set_widget_mapsize)
    
    
    
    def get_marker_icons(self):
        return getattr(self.context, PROPERTY_MARKERS, '')

    def set_marker_icons(self, value):
        self.context._updateProperty(PROPERTY_MARKERS, value)

    marker_icons = property(get_marker_icons, set_marker_icons)    



class MapsControlPanel(ControlPanelForm):

    form_fields = FormFields(IMapsSchema)
    label = _("Product settings")
    description = None
    form_name = _("Parameters configuration")
