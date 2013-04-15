from django.conf.urls import patterns, include, url


urlpatterns = patterns('kiosk.views',
    url(r'^$', 'home', name="home"),
    url(r'^items/(?P<id_exhibition>\d+)/$', 'exhibit_item_list',
        name="exhibit_item_list")
)
