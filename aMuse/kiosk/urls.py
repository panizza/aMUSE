from django.conf.urls import patterns, include, url


urlpatterns = patterns('kiosk.views',
    url(r'^$', 'home', name="home")
)
