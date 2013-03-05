from django.conf.urls import patterns, include, url
from piston.resource import Resource
from api.handlers import ItemHandler

item_handler = Resource(ItemHandler)

urlpatterns = patterns('api.views',
    #url(r'^info/(?P<id>\d+)/$$', item_handler, name='obtain_item_info'),
    url(r'^info/(?P<item_id>\d+)/$', item_handler),
)
