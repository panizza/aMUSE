from django.conf.urls import patterns, include, url


urlpatterns = patterns('api.views',
    url(r'^i/(?P<id_item>\d+)/$', 'get_item_info',
        name="get_item_info"),
    url(r'^exp/s/$', 'save_experience',
        name="save_experience"),

    ######################################
    ##### ONLY FOR DEBUG! DO NOT EDIT#####
    ######################################
    url(r'^test/$', 'api_test_for_some_code')
)
