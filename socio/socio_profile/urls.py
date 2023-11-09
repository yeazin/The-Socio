"""

Socio Profile Urls 

"""
from django.urls import path
from socio_profile.views import (
    SocioPostSelfListView
)

urlpatterns = [
    path("self/post/list/view/", SocioPostSelfListView.as_view())
]