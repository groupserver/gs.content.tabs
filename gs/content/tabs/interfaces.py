# coding=utf-8
from zope.viewlet.interfaces import IViewlet
from zope.schema import Bool, Choice, Int, List, Text, TextLine

class IGSTab(IViewlet):
    title = TextLine(title=u'Title',
                description=u'The the text for the tab-control itself.',
                requried=True)
    
    weight = Int(title=u'Weight',
                description=u'Order of the tab in the controls.',
                requried=True)

    

