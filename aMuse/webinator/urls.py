from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('webinator.views',
        url(r'^$', 'index', name='index'),
        url(r'^login/', login,  name='login'),
        url(r'^logout/', logout, {'next_page': '/webinator/'}, name='logout'),
)
