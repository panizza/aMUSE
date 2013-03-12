from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('webinator.views',
        url(r'^login/', login, name='login'),
        url(r'^logout/', logout, name='logout'),
)
