from django.conf.urls import patterns, include, url


urlpatterns = patterns('api.views',
    url(r'^i/(?P<hash_item>[a-f0-9]{40})/$', 'get_item_info', name="get_item_info"),
    url(r'^e/list/$', 'exhibition_list', name='exhibition_list'),
    url(r'^exp/s/$', 'save_experience', name="save_experience"),

    ######################################
    ##### ONLY FOR DEBUG! DO NOT EDIT#####
    ######################################
    url(r'^test/$', 'api_test_for_some_code')
)
