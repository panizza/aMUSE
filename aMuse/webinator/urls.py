from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
#from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = patterns('webinator.views',
        url(r'^$', 'index', name='index'),
        url(r'^login/', login,  name='login'),
        url(r'^logout/', logout, {'next_page': '/webinator/'}, name='logout'),

        url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
         'reset_password_new_user', name='reset_password_new_user')
)
