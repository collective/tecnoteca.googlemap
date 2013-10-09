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

from zope.component import getMultiAdapter

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
        helper = getMultiAdapter((self.context, self.request), name=u'ttgooglemap_helpersview')
        context = aq_inner(self.context)
        markers = []
        try:
            related = []            
            # add direct relations
            related.extend(context.computeRelatedItems())
            # add inverse relations
            related.extend(context.getBRefs())
            for rel in related:
                if(rel.portal_type == 'TTGoogleMapMarker'): # helper.isGMContentType(rel)
                    markers.append(rel)
        except:
            pass
        return markers
    
class AddForm(base.NullAddForm):
    
    def create(self):
        return Assignment()
