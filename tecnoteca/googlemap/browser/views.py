from Products.Five.browser import BrowserView
from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.CMFCore.permissions import View
from zope.interface import implements
from tecnoteca.googlemap.interfaces.views import IHelpersView
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from plone.memoize.view import memoize

class HelpersView(BrowserView):
    """ Utility class """
    
    implements(IHelpersView)
    
    security = ClassSecurityInfo()
    
    security.declareProtected(View,'customEscape')
    def customEscape(self, text):
        text = text.replace('"','\\"')
        text = text.replace("\r", "")
        text = text.replace("\n", "")
        text = unicode(text, errors='ignore')
        return text    


    security.declareProtected(View,'isGMContentType')
    def isGMContentType(self, object):
        """ tecnoteca.googlemap content-type """
        return object.portal_type == 'TTGoogleMapMarker' \
            or object.portal_type == 'TTGoogleMapPolygon' \
            or object.portal_type == 'TTGoogleMapPolyline' 
        
    
    security.declareProtected(View,'getTitleHTML')
    def getTitleHTML(self, object):
        output = "" 
        if self.isGMContentType(object):
            output += "<b>"+self.customEscape(object.Title())+"</b><br/>"
        else: # other content-type obj
            output += "<a href='"+object.absolute_url()+"'><b>"+self.customEscape(object.Title())+"</b></a><br/>"            
        return output
        

                
    security.declareProtected(View,'getDescriptionHTML')
    def getDescriptionHTML(self, object):
        output = ""
        if self.isGMContentType(object) and hasattr(object, "getText"):
            output = (self.customEscape(object.getText())).strip()            
        else:
            output = (self.customEscape(object.Description())).strip()
        return output        
 
    
    security.declareProtected(View,'getRelatedItemsHTML')
    def getRelatedItemsHTML(self, object):
        ctool = getToolByName(self.context, 'portal_catalog')
        # backref items
        query_br = self.query().copy()
        query_br['getRawRelatedItems'] = object.UID()
        items = ctool(query_br)
        # related items
        if object.getRawRelatedItems():
            query_r = self.query().copy()
            query_r['UID'] = object.getRawRelatedItems()
            items += ctool(query_r)
        output = ""
        if items:
            output += "<ul>"
            for item in items:
                output += "<li>"
                output += "<a href='%(url)s' title='%(title)s'>%(title)s</a>" % {'url': item.getURL(), 
                                                                                 'title': item.pretty_title_or_id()}
                output += "</li>"
            output += "</ul>"
        return output
    
    @memoize
    def query(self):
        ptool = getToolByName(self.context, "portal_properties")
        navtree = getattr(ptool, "navtree_properties")
        query = dict(sort_on = 'sortable_title',
                     expired = {'query': DateTime(), 'range': 'min'})
        if navtree.getProperty('enable_wf_state_filtering', False):
            query['review_state'] = navtree.getProperty('wf_states_to_show', ())
        return query