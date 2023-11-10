"""

Socio Profile Urls 

"""
from django.urls import path, include
from socio_profile.views import (
    SocioPostSelfListView,
    SocioProfileSelfView,
    SocioProfileSelfUpdateView,
    SocioProfileListView,

    SocialLinksCreateView,
    SocialLinksSelfUpdateView,
    SocialLinkseSelfView,
    SocioFollowUnfollowView
)

app_name = "socian_profile"

self_url = [
    path("post/list/view/", SocioPostSelfListView.as_view()),
    path("view/", SocioProfileSelfView.as_view()),
    path("update/view/", SocioProfileSelfUpdateView.as_view()),
]

social_links_url = [
    path("create/", SocialLinksCreateView.as_view()),
    path("self/update/", SocialLinksSelfUpdateView.as_view()),
    path("self/view/", SocialLinkseSelfView.as_view()),
]

socio_url = [
    path("list/", SocioProfileListView.as_view()),
    path("follow/unfollow/", SocioFollowUnfollowView.as_view()),
]

urlpatterns = [
    path("self/", include(self_url)),
    path("", include(socio_url)),
    path("social-links/", include(social_links_url)),
]