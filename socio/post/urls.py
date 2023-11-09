"""

Post Urls 

"""

from django.urls import path
from post.views import (
    SocioPostCreateView,
    SocioPostListView,
    SocioPostDetailedView,
    SocioPostFuncsView
)

app_name = "post"

urlpatterns = [
    path("create/", SocioPostCreateView.as_view()),
    path("list/", SocioPostListView.as_view()),
    path("view/<str:pk>/", SocioPostDetailedView.as_view()),
    path("funcs/<str:pk>/", SocioPostFuncsView.as_view()),
]