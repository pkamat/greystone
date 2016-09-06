from django.conf.urls import url

import views

urlpatterns = [
    url(r'^messages$', views.rest_view, name='messages'),
    url(r'^messages/(?P<id>\d+)$', views.rest_view, name='messages'),
]
