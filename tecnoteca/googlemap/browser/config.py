from zope.interface import implements
from Products.Five.browser import BrowserView
from Products.Five.formlib import formbase
from tecnoteca.googlemap.config import *
from tecnoteca.googlemap.interfaces.config import ITTGoogleMapConfig
from tecnoteca.googlemap.validator import LocationFieldValidator
from Products.CMFCore.utils import getToolByName
from zope.i18nmessageid import MessageFactory
from zope.formlib import form
from zope.interface import implements
from zope.schema.fieldproperty import FieldProperty
from OFS.SimpleItem import SimpleItem
from zope.component import getUtility

_ = MessageFactory('tecnoteca.googlemap')

class TTGoogleMapConfig(BrowserView):

    implements(ITTGoogleMapConfig)

    def __init__(self, context, request):
        """ init view """
        self.context = context
        self.request = request
        portal_props = getToolByName(context, 'portal_properties')
        self.properties = getattr(portal_props, PROPERTY_SHEET, None)

    def _search_key(self, property_id):        
        if self.properties is None:
            return 'undefined'
        keys_list = getattr(self.properties, property_id, None)
        if keys_list is None:
            return 'undefined'
        keys = {}
        for key in keys_list:
            url, key = key.split('|')
            url = url.strip()
            # remove trailing slashes
            url = url.strip('/')
            key = key.strip()
            keys[url] = key
        portal_url_tool = getToolByName(self.context, 'portal_url')
        portal_url = portal_url_tool()
        portal_url = portal_url.split('/')
        while len(portal_url) > 2:
            url = '/'.join(portal_url)
            if keys.has_key(url):
                return keys[url]
            portal_url = portal_url[:-1]
        return 'undefined'
    
    @property
    def coord_widget_map_size(self):
        if self.properties is None:
            return 'undefined'
        size = getattr(self.properties, PROPERTY_COORD_WIDGET_MAP_SIZE, None)
        if size is None:
            return 'undefined'        
        split = size.split(',')
        return (split[0], split[1])
    
    @property
    def default_map_size(self):
        if self.properties is None:
            return 'undefined'
        size = getattr(self.properties, PROPERTY_DEFAULT_MAPSIZE, None)
        if size is None:
            return 'undefined'        
        split = size.split(',')
        return (split[0], split[1])

    @property
    def googlemaps_key(self):
        return self._search_key(PROPERTY_GOOGLE_KEYS)

    @property
    def marker_icons(self):
        if self.properties is None:
            return {}
        icons_list = getattr(self.properties, PROPERTY_MARKERS, None)
        if icons_list is None:
            return {}
        portal_url_tool = getToolByName(self.context, 'portal_url')
        portal_url = portal_url_tool()
        icons = []
        for icon in icons_list:
            parts = icon.split("|")
            icons.append((parts[0], parts[1]))
        return icons

    @property
    def default_location(self):
        if self.properties is None:
            return (0.0, 0.0)
        default_location = getattr(self.properties,
                                   PROPERTY_DEFAULT_LOCATION,
                                   (0.0, 0.0))
        if isinstance(default_location, basestring):
            default_location = default_location.split(',')
        validator = LocationFieldValidator('default_location')
        if validator(default_location) != 1:
            return (0.0, 0.0)
        return default_location