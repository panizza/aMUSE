from django.conf.urls import patterns, include, url


urlpatterns = patterns('kiosk.views',
    url(r'^$', 'home', name="home"),
    url(r'^item/(?P<id_item>\d+)/info/$', 'item_info', name="item_info"),
    url(r'^items/(?P<id_exhibition>\d+)/$', 'exhibit_item_list',
        name="exhibit_item_list")
)
