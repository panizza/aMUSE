from django.conf.urls import patterns, include, url
from api.views import get_item, save_visit


urlpatterns = patterns('api.views',
    url(r'^info/(?P<id_item>\d+)/$', 'get_item', name="get_info"),
    url(r'^save/$', 'save_visit', name="save_visit"),
)
