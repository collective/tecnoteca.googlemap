Tecnoteca GoogleMap Module for Plone 3 and Plone 4
---------------------------------------------------------------------------

The Tecnoteca GoogleMap module and these instructions are distributed
in the hope that they will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.

Tecnoteca does not guarantee that there will be no damage to your
existing Plone installation when using this module.

IMPORTANT: Before using this module, make sure you have a full backup
of your Plone installation.

**************************************************************************


Introduction
---------------------------------------------------------------------------
This product lets you include Google Maps v3 in a Plone 3 / Plone 4 environment.
The Tecnoteca GoogleMap module extends Plone with the capability to display different maps with macro-categories, categories, markers, paths and areas.
Thanks to the Plone relations feature it's possible to define georeference from/to map markers and other Plone objects.
You can also extend your custom content types (Archetypes) to add geolocalization attributes and then show your content types on the google map.

.. image:: http://www.tecnoteca.com/it/release/plone-google-map/immagini/TecnotecaGoogleMap.png/image_preview


Features
---------------------------------------------------------------------------
- Plone 3 and Plone 4 compatibility
- Complete map definition (center,zoom,size,advanced controls,traffic,panoramio,weather,bicycle,street view, etc)
- Custom categories with custom icons and unlimited markers per category
- Location widget to define markers' position
- Georeference for custom content types (Archetypes), see section below
- Georeference for plone pages, events, news, images etc
- Custom paths
- Custom areas
- Portlet to show georeference relations
- Cache load option (@ram.cache)
- Italian, English and French localizations

**Scenario**

You have a Plone site and you'd like to add several maps (culture, health, 
transportation, etc) each one containing several categories (ie museums, 
theaters, churches etc), and every category containing several markers 
(ie museum n.1, museum n.2, museum n.3 etc).

Moreover you'd like to link together the content page regarding the "museum n.1" 
and the marker "museum n.1" you've defined in your map, so that a user reading 
the content page could see where that specific museum is located.

Also, you have your custom content types and you would like to extend them with 
georeference feature so that you can show them on a google map.

Finally, you'd like to highlight some areas of your city / territory (ie highlight 
residential area) and highlight some paths (ie highlight streets or tourist routes).


Usage
---------------------------------------------------------------------------
Once you've installed and configured the product you can create a google map object.
Then, inside the google map object, you can create paths / areas / categories and, inside categories, markers.
Important: you must publish categories / markers / paths / areas to show them on the map!

Example:

1. Add new >> Google Map
2. (inside Google Map object) Add new >> Google Map Category
3. (inside Google Map Category) Add new >> Google Map Marker
4. **Publish your categories and markers in order to see them on the map**

If you'd like to add the "related markers" portlet please use the Plone portlet manager ( http://path_to_your_installation/@@manage-portlets ).


Extend your custom content types (Archetype)
---------------------------------------------------------------------------
1. Import:

    **from tecnoteca.googlemap.content.ttgooglemapcoordinates import TTGoogleMapCoordinates,TTGoogleMapCoordinatesSchema**

2. Extend schema:
    schemata.ATContentTypeSchema.copy() + atapi.Schema((
        ...

    )) + **TTGoogleMapCoordinatesSchema.copy()**

3. Extend class:
    class MyContentType(base.ATCTContent, **TTGoogleMapCoordinates**):

4. Done! Now your content type has the required georeference fields and you can edit your items to set location

5. Add to your GoogleMap a new "Google Map Category Content Type" object to show your items on the map


Requirements
---------------------------------------------------------------------------
- Plone 3 / 4
- SmartColorWidget


Configuration
---------------------------------------------------------------------------
Before creating a GoogleMap object please configure product parameters in plone control panel (http://path_to_your_installation/plone_control_panel).

The google map api key can be generated here: http://code.google.com/apis/maps/signup.html


Installation
---------------------------------------------------------------------------
Standard buildout installation, see docs/INSTALL.txt


Support and issues
---------------------------------------------------------------------------
http://www.tecnoteca.com/en/contact


Author
---------------------------------------------------------------------------
Tecnoteca srl
Via l'Aquila, 1/B
33010 Tavagnacco UD
http://www.tecnoteca.com