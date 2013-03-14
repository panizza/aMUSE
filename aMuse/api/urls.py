from django.conf.urls import patterns, include, url


urlpatterns = patterns('api.views',
    url(r'^info/(?P<id_item>\d+)/$', 'get_item', name="get_info"),
    url(r'^save/$', 'visit_save', name="save_visit")
)
