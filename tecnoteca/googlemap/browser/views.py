from Products.Five.browser import BrowserView
from AccessControl.SecurityInfo import ClassSecurityInfo
from Products.CMFCore.permissions import View
from zope.interface import implements
from tecnoteca.googlemap.interfaces.views import IHelpersView
from DateTime import DateTime

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
        output = ""        
        if object.getRelatedItems() or object.getBRefs():
            output += "<ul>"
            for relation in object.getRelatedItems(): # A>B relation
                if relation and (not hasattr(relation, 'getLanguage') or relation.getLanguage()==context.REQUEST.get("Language","it")) and relation.expires() > DateTime():
                    output += "<li>"
                    output += "<a href='"+relation.absolute_url()+"' title='"+self.customEscape(relation.Title())+"'>"+self.customEscape(relation.Title())+"</a>"
                    output += "</li>"
            for relation in object.getBRefs(): # B>A relation
                if relation and relation.expires() > DateTime():
                    output += "<li>"
                    output += "<a href='"+relation.absolute_url()+"' title='"+self.customEscape(relation.pretty_title_or_id())+"'>"+self.customEscape(relation.pretty_title_or_id())+"</a>"
                    output += "</li>"
            output += "</ul>"
        return output
            