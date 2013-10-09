from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.view import memoize

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName


class CTLinkViewlet(ViewletBase):
    """ Viewlet to show web links to google maps objects containing current content-type """
    
    render = ViewPageTemplateFile('viewlet_ct_link.pt')
    
    @property
    def show(self):
        if hasattr(self.context, "getCoordinates") and self.context.getCoordinates() and len(self.items()):
            return True
        return False
    
    @memoize
    def items(self):
        # create query
        query = dict(gmap_category_objecttype = self.context.portal_type,
                     sort_on = 'sortable_title')
        # state
        properties = getToolByName(self.context, 'portal_properties')
        navtree_properties = getattr(properties, "navtree_properties")
        if navtree_properties.getProperty("enable_wf_state_filtering", False):
            query['review_state'] = navtree_properties.getProperty("wf_states_to_show", ())
        # query catalog
        catalog = getToolByName(self.context, 'portal_catalog')
        brains = catalog(query)
        # get site encoding
        site_properties = getattr(properties, "site_properties")
        encoding = site_properties.getProperty("default_charset", "utf-8")
        # create list of dictionaries
        items = list()
        for brain in brains:
            object = brain.getObject()
            map = object.getParentMap()
            if map is not None:
                items.append(dict(title = map.Title().decode(encoding, "ignore"),
                                  description = map.Description().decode(encoding, "ignore"),
                                  url = "%s?mk=%s" % (map.absolute_url(), self.context.UID())))
        return items