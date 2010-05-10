"""Common configuration constants
"""

PROJECTNAME = 'tecnoteca.googlemap'

PROPERTY_SHEET = 'ttgooglemap_properties'
PROPERTY_GOOGLE_KEYS = 'ttgooglemap_api_keys'
PROPERTY_DEFAULT_LOCATION = 'ttgooglemap_default_location'
PROPERTY_DEFAULT_MAPSIZE = 'ttgooglemap_default_map_size'
PROPERTY_COORD_WIDGET_MAP_SIZE = 'ttgooglemap_coord_widget_map_size'
PROPERTY_MARKERS = 'ttgooglemap_markers'

ADD_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'TTGoogleMapPolygon': 'tecnoteca.googlemap: Add TTGoogleMapPolygon',
    'TTGoogleMapPolyline': 'tecnoteca.googlemap: Add TTGoogleMapPolyline',
    'TTGoogleMapMarker': 'tecnoteca.googlemap: Add TTGoogleMapMarker',
    'TTGoogleMapCategory': 'tecnoteca.googlemap: Add TTGoogleMapCategory',
    'TTGoogleMapCategoryContainer': 'tecnoteca.googlemap: Add TTGoogleMapCategoryContainer',
    'TTGoogleMap': 'tecnoteca.googlemap: Add TTGoogleMap',
}