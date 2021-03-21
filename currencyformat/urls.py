from django.conf.urls import url 
from currencyformat import views 
 
urlpatterns = [ 
    #url(r'^api/worldcurrencyformat$', views.worldcurrencyformat_list),
    url(r'^worldcurrencyformat/(?P<id>[0-9]+)$', views.worldcurrencyformat_detail),
    url(r'^worldcurrencyformat/$', views.worldcurrencyformat_read, name='worldcurrencyformat_read'),
    url(r'^worldcurrencyformat/test$', views.worldcurrencyformat_test, name='worldcurrencyformat_test'),
    url(r'^worldcurrencyformat/create$', views.worldcurrencyformat_create, name='worldcurrencyformat_create'),
    url(r'^worldcurrencyformat/update$', views.worldcurrencyformat_update, name='worldcurrencyformat_update'),
    url(r'^worldcurrencyformat/delete$', views.worldcurrencyformat_delete, name='worldcurrencyformat_delete'),
    #url(r'^api/worldcurrencyformat/published$', views.tutorial_list_published)
]