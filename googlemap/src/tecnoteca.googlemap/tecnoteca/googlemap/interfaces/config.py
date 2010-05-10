from zope.interface import Interface
from zope.interface import Attribute


class ITTGoogleMapConfig(Interface):
    """Interface to the configuration of TTGoogleMaps
    """
    googlemaps_key = Attribute("The API key for Google Maps for the current portal URL")
    marker_icons = Attribute("A list of markers")
    default_location = Attribute("The default coordinates for new locations")
    default_map_size = Attribute("The default map size")
    coord_widget_map_size = Attribute("The default coordinates widget map size")