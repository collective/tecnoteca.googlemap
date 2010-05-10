from zope.interface import implements
from zope.component import adapts, getMultiAdapter, queryUtility

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope.i18nmessageid import MessageFactory

from zope import schema
from zope.formlib import form
from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

_ = MessageFactory('tecnoteca.googlemap')

class ITTGeoReferencePortlet(IPortletDataProvider):
    """A portlet that renders geo reference links"""
    
class Assignment(base.Assignment):
    implements(ITTGeoReferencePortlet)
    
    @property
    def title(self):
        return _(u"Google Map related markers")

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('TTGeoReference.pt')
        
    def getRelatedMarkers(self):
        context = aq_inner(self.context)
        try:
            related = context.computeRelatedItems();
            markers = []
            for rel in related:
                if(rel.portal_type == 'TTGoogleMapMarker'):
                    markers.append(rel)
        except:
            pass
    
class AddForm(base.NullAddForm):
    
    def create(self):
        return Assignment()
