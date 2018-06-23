from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from items import views

urlpatterns = [
    url(r'^items/$', views.ItemList.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    path('items/update/<int:item_id>', views.update_status),
]


urlpatterns = format_suffix_patterns(urlpatterns)
