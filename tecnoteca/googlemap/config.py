"""Common configuration constants
"""

PROJECTNAME = 'tecnoteca.googlemap'

PROPERTY_SHEET = 'ttgooglemap_properties'
PROPERTY_SHEET_TITLE = 'TTGoogleMap Properties'
PROPERTY_GOOGLE_KEYS = 'ttgooglemap_api_keys'
PROPERTY_DEFAULT_LOCATION = 'ttgooglemap_default_location'
PROPERTY_DEFAULT_MAPSIZE = 'ttgooglemap_default_map_size'
PROPERTY_COORD_WIDGET_MAP_SIZE = 'ttgooglemap_coord_widget_map_size'
PROPERTY_MARKERS = 'ttgooglemap_markers'
PROPERTY_MARKERS_CACHE = 'ttgooglemap_markers_cache'

ADD_PERMISSIONS = {
    # -*- extra stuff goes here -*-
    'TTGoogleMapPolygon': 'tecnoteca.googlemap: Add TTGoogleMapPolygon',
    'TTGoogleMapPolyline': 'tecnoteca.googlemap: Add TTGoogleMapPolyline',
    'TTGoogleMapMarker': 'tecnoteca.googlemap: Add TTGoogleMapMarker',
    'TTGoogleMapCategory': 'tecnoteca.googlemap: Add TTGoogleMapCategory',
    'TTGoogleMapCategoryCT': 'tecnoteca.googlemap: Add TTGoogleMapCategoryCT',
    'TTGoogleMapCategoryContainer': 'tecnoteca.googlemap: Add TTGoogleMapCategoryContainer',
    'TTGoogleMap': 'tecnoteca.googlemap: Add TTGoogleMap',
}

PROPERTIES_LIST = [{'id' : PROPERTY_GOOGLE_KEYS, 'type' : 'lines', 'value' : ["http://localhost:8080 |","www.mydomain.com|google_map_key"]},
                   {'id' : PROPERTY_DEFAULT_LOCATION, 'type' : 'string', 'value' : '46.10857,13.22452'},
                   {'id' : PROPERTY_DEFAULT_MAPSIZE, 'type' : 'string', 'value' : '400,600'},
                   {'id' : PROPERTY_COORD_WIDGET_MAP_SIZE, 'type' : 'string', 'value' : '400,450'},
                   {'id' : PROPERTY_MARKERS, 'type' : 'lines', 'value' : ["marker_accident.png|accident",\
                                                                        "marker_airplane-tourism.png|airplane-tourism",\
                                                                        "marker_ancientmonument.png|ancientmonument",\
                                                                        "marker_ancienttemple.png|ancienttemple",\
                                                                        "marker_animals.png|animals",\
                                                                        "marker_aquarium.png|aquarium",\
                                                                        "marker_archery.png|archery",\
                                                                        "marker_arch.png|arch",\
                                                                        "marker_artgallery.png|artgallery",\
                                                                        "marker_bankeuro.png|bankeuro",\
                                                                        "marker_bar.png|bar",\
                                                                        "marker_beach.png|beach",\
                                                                        "marker_bicycleparking.png|bicycleparking",\
                                                                        "marker_bookstore.png|bookstore",\
                                                                        "marker_bus.png|bus",\
                                                                        "marker_camping.png|camping",\
                                                                        "marker_car.png|car",\
                                                                        "marker_cathedral.png|cathedral",\
                                                                        "marker_cemetary.png|cemetary",\
                                                                        "marker_cinema.png|cinema",\
                                                                        "marker_clothes.png|clothes",\
                                                                        "marker_cluster3.png|cluster3",\
                                                                        "marker_coffee.png|coffee",\
                                                                        "marker_communitycentre.png|communitycentre",\
                                                                        "marker_company.png|company",\
                                                                        "marker_computer.png|computer",\
                                                                        "marker_construction.png|construction",\
                                                                        "marker_country.png|country",\
                                                                        "marker_court.png|court",\
                                                                        "marker_customs.png|customs",\
                                                                        "marker_cyclingsport.png|cyclingsport",\
                                                                        "marker_dancinghall.png|dancinghall",\
                                                                        "marker_daycare.png|daycare",\
                                                                        "marker_disability.png|disability",\
                                                                        "marker_dog-offleash.png|dog-offleash",\
                                                                        "marker_factory.png|factory",\
                                                                        "marker_family.png|family",\
                                                                        "marker_farm.png|farm",\
                                                                        "marker_fastfood.png|fastfood",\
                                                                        "marker_festival.png|festival",\
                                                                        "marker_firstaid.png|firstaid",\
                                                                        "marker_fitnesscenter.png|fitnesscenter",\
                                                                        "marker_flowers.png|flowers",\
                                                                        "marker_forest.png|forest",\
                                                                        "marker_fountain.png|fountain",\
                                                                        "marker_gazstation.png|gazstation",\
                                                                        "marker_gym.png|gym",\
                                                                        "marker_highway.png|highway",\
                                                                        "marker_home.png|home",\
                                                                        "marker_hotel.png|hotel",\
                                                                        "marker_info.png|info",\
                                                                        "marker_jogging.png|jogging",\
                                                                        "marker_justice.png|justice",\
                                                                        "marker_lake.png|lake",\
                                                                        "marker_library.png|library",\
                                                                        "marker_lighthouse.png|lighthouse",\
                                                                        "marker_lock.png|lock",\
                                                                        "marker_massage.png|massage",\
                                                                        "marker_mine.png|mine",\
                                                                        "marker_monument.png|monument",\
                                                                        "marker_movierental.png|movierental",\
                                                                        "marker_museum-archeological.png|museum-archeological",\
                                                                        "marker_museum-art.png|museum-art",\
                                                                        "marker_museum-crafts.png|museum-crafts",\
                                                                        "marker_museum-historical.png|museum-historical",\
                                                                        "marker_museum.png|museum.png",\
                                                                        "marker_museum-science.png|museum-science",\
                                                                        "marker_music-classical.png|music-classical",\
                                                                        "marker_music.png|music",\
                                                                        "marker_nanny.png|nanny",\
                                                                        "marker_newsagent.png|newsagent",\
                                                                        "marker_nursery.png|nursery",\
                                                                        "marker_olympicsite.png|olympicsite",\
                                                                        "marker_parking.png|parking",\
                                                                        "marker_party.png|party",\
                                                                        "marker_photo.png|photo",\
                                                                        "marker_picnic.png|picnic",\
                                                                        "marker_playground.png|playground",\
                                                                        "marker_police2.png|police2",\
                                                                        "marker_police.png|police",\
                                                                        "marker_pool.png|pool",\
                                                                        "marker_restaurantgourmet.png|restaurantgourmet",\
                                                                        "marker_restaurant.png|restaurant",\
                                                                        "marker_sailboat-sport.png|sailboat-sport",\
                                                                        "marker_school.png|school",\
                                                                        "marker_sciencecenter.png|sciencecenter",\
                                                                        "marker_seniorsite.png|seniorsite",\
                                                                        "marker_sight.png|sight",\
                                                                        "marker_steamtrain.png|steamtrain",\
                                                                        "marker_subway.png|subway",\
                                                                        "marker_suv.png|suv",\
                                                                        "marker_taxiway.png|taxiway",\
                                                                        "marker_telephone.png|telephone",\
                                                                        "marker_theater.png|theater",\
                                                                        "marker_themepark.png|themepark",\
                                                                        "marker_toilets.png|toilets",\
                                                                        "marker_tools.png|tools",\
                                                                        "marker_toys.png|toys",\
                                                                        "marker_train.png|train",\
                                                                        "marker_trash.png|trash",\
                                                                        "marker_university.png|university",\
                                                                        "marker_vespa.png|vespa",\
                                                                        "marker_videogames.png|videogames",\
                                                                        "marker_video.png|video",\
                                                                        "marker_water.png|water",\
                                                                        "marker_wedding.png|wedding",\
                                                                        "marker_wifi.png|wifi",\
                                                                        "marker_winery.png|winery",\
                                                                        "marker_workoffice.png|workoffice",\
                                                                        "marker_world.png|world",\
                                                                        "marker_youthhostel.png|youthhostel",\
                                                                        "marker_zoo.png|zoo"]},
                   {'id' : PROPERTY_MARKERS_CACHE, 'type' : 'int', 'value' : 0},]