"""

Post Urls 

"""

from django.urls import path, include
from post.views import (
    SocioPostCreateView,
    SocioPostListView,
    SocioPostDetailedView,
    SocioPostFuncsView,

    SocioPostCommentCreateView,
    SocioPostCommentFuncsView,

    SocioBridgeofPostUserCreateView,
    SocioBridgeofPostUserDeleteView
)

app_name = "post"

post_url = [
    path("create/", SocioPostCreateView.as_view()),
    path("list/", SocioPostListView.as_view()),
    path("view/<str:pk>/", SocioPostDetailedView.as_view()),
    path("funcs/<str:pk>/", SocioPostFuncsView.as_view()),
]

comment_url = [
    path("create/", SocioPostCommentCreateView.as_view()),
    path("funcs/<str:pk>/", SocioPostCommentFuncsView.as_view()),
]


bridge_post_likes_url = [
    path("post-likes/create/", SocioBridgeofPostUserCreateView.as_view()),
    path("post-likes/delete/", SocioBridgeofPostUserDeleteView.as_view())
]


urlpatterns = [
    path('', include(post_url)),
    path('comment/', include(comment_url)),
    path('bridge/', include(bridge_post_likes_url))
]