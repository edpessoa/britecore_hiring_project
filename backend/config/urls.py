from django.urls import path

from django.conf.urls import include

from config.api import api


urlpatterns = [
    path("api/", include(api.urls)),
]
