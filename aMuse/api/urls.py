from django.conf.urls import patterns, include, url

urlpatterns = patterns('api.views',
    url(r'^info/(?P<id>\d+)/$$', 'obtain_item_info', name='obtain_item_info'),
)
