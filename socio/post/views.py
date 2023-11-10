
"""
Post Views 
"""

from rest_framework import (
    generics,
    filters
)
from rest_framework.throttling import (
    UserRateThrottle,
    AnonRateThrottle
)
from util_base.utils._permission import IsSocian
from socio_profile.models import SocioUser
from post.models import (
    SocioPost,
    SocioPostComment,
    BridgeOfPostUserLikes
)

from post.serializers import (
    SocioPostFuncsSerializer,
    SocioPostDetailedSerializer,
    SocioCommentFuncsSerializer,
    SocioBridgeofPostAndUserSerializer
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
    # search Functionality 
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "post_title",
        "post_description",
        "post_author__full_name"
    ]


## Post of List view of Followers 

class SocioPostListViewofFollowersView(generics.ListAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioPostDetailedSerializer

    # search Functionality
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "post_title",
        "post_description",
        "post_author__full_name"
    ]

    # Getting the current logged in Socio User
    def get_current_socian(self):
        return self.request.user.socio
    
    def get_queryset(self):

        # getting the current socio User followers list
        current_socio_user_followers_list = SocioUser.objects.filter(
            id=self.get_current_socian().id).first().follows.values("id")
        
        # returning the followers post
        return SocioPost.objects.filter(
            post_author__in=current_socio_user_followers_list
            ).select_related(
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



###### ####### ####
### Socio Comment Views


class SocioPostCommentCreateView(generics.CreateAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioCommentFuncsSerializer
    queryset = SocioPostComment.objects.filter()


## Read, Update , Delete View 
class SocioPostCommentFuncsView(generics.RetrieveUpdateDestroyAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioCommentFuncsSerializer
    queryset = SocioPostComment.objects.filter()




###### ####### ####
### Socio Post and Likes Bridge Views

## The following views will be hidden functionlities 
## Becaues these views are only create and delete view 
## Frontend devs will utilize these views in some point
## that the end user don`t see the changes 

# Create View  

class SocioBridgeofPostUserCreateView(generics.CreateAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioBridgeofPostAndUserSerializer
    queryset = BridgeOfPostUserLikes.objects.filter()


# Delete View 

class SocioBridgeofPostUserDeleteView(generics.DestroyAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioBridgeofPostAndUserSerializer
    queryset = BridgeOfPostUserLikes.objects.filter()