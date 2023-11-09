
"""
Post Views 
"""

from rest_framework import generics
from rest_framework.throttling import (
    UserRateThrottle,
    AnonRateThrottle
)
from util_base.utils._permission import IsSocian
from post.models import (
    SocioPost,
    SocioPostComment,
    BridgeOfPostUserLikes
)

from post.serializers import (
    SocioPostFuncsSerializer,
    SocioPostDetailedSerializer
)


import logging

logger = logging.getLogger(__name__)


###### ####### ####
### Socio Post Views 


## Create View 
class SocioPostCreateView(generics.CreateAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioPostFuncsSerializer
    queryset = SocioPost.objects.filter()


## List View
class SocioPostListView(generics.ListAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioPostDetailedSerializer
    queryset = SocioPost.objects.select_related(
        "post_author",
    ).order_by(
        "-created_at"
    )


## Post Detailed View 
class SocioPostDetailedView(generics.RetrieveAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioPostDetailedSerializer
    queryset = SocioPost.objects.select_related(
        "post_author",
    ).order_by(
        "-created_at"
    )


## Update, Delete View 
class SocioPostFuncsView(generics.RetrieveUpdateDestroyAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioPostFuncsSerializer
    queryset = SocioPost.objects.filter()