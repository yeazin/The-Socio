"""

Socio Profile Urls 

"""
from django.urls import path
from socio_profile.views import (
    SocioPostSelfListView,
    SocioProfileSelfView,
    SocioProfileSelfUpdateView
)

urlpatterns = [
    path("self/post/list/view/", SocioPostSelfListView.as_view()),
    path("self/view/", SocioProfileSelfView.as_view()),
    path("self/update/view/", SocioProfileSelfUpdateView.as_view()),
]