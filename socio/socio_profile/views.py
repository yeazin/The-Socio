
"""
Socio Profile Views 
"""
import uuid
from rest_framework import (
    generics, 
    response
)
from rest_framework.throttling import (
    UserRateThrottle,
    AnonRateThrottle
)
from util_base.utils._permission import IsSocian
from socio_profile.models import (
    SocioUser,
    SocialLinks
)
from post.models import (
    SocioPost
)
from socio_profile.serialilzers import (
    SocioPostSelfSocianSerializer,
    SocioProfileFuncsSerializer,
    SocioProfileDetailedSerializer,
    SocialLinkSerializer,
    SocioFollowUnfollowSerializer
)


import logging

logger = logging.getLogger(__name__)



###### ####### ####
### Socio profile Views 


## Socio Profile Self View 

class SocioProfileSelfView(generics.GenericAPIView):

    throttle_classes = [UserRateThrottle]
    serializer_class = SocioProfileFuncsSerializer
    permission_classes = [IsSocian]

    def get(self,request):
        serializer = SocioProfileDetailedSerializer(request.user.socio)
        return response.Response(serializer.data)
    

## Socio Profile Self Update View 

class SocioProfileSelfUpdateView(generics.UpdateAPIView):

    throttle_classes = [UserRateThrottle]
    serializer_class = SocioProfileFuncsSerializer
    permission_classes = [IsSocian]

    def get_object(self):
        return self.request.user.socio


## Socio User list view 

class SocioProfileListView(generics.ListAPIView):

    throttle_classes = [UserRateThrottle]
    serializer_class = SocioProfileDetailedSerializer
    permission_classes = [IsSocian]
    queryset = SocioUser.objects.filter()


###### ####### ####
### Social Links  Views


# Social Links Create View 

class SocialLinksCreateView(generics.CreateAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocialLinkSerializer
    queryset = SocialLinks.objects.filter().select_related(
        "socio_user"
    )



# Social Links Update View 
class SocialLinksSelfUpdateView(generics.UpdateAPIView):

    throttle_classes = [UserRateThrottle]
    serializer_class = SocialLinkSerializer
    permission_classes = [IsSocian]
    queryset = SocialLinks.objects.filter()

    def get_object(self):
        return self.request.user.socio

# Social Links Self View 
class SocialLinkseSelfView(generics.ListAPIView):

    throttle_classes = [UserRateThrottle]
    serializer_class = SocialLinkSerializer
    permission_classes = [IsSocian]

    
    def get_current_socian(self):
        return self.request.user.socio
    
    def get_queryset(self):
        return SocialLinks.objects.filter(
            socio_user=self.get_current_socian()
        ).order_by(
            "-created_at"
        )



###### ####### ####
### Socio Post self profile Views 

class SocioPostSelfListView(generics.ListAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioPostSelfSocianSerializer
    queryset = SocioPost.objects.select_related(
        "post_author",
    ).order_by(
        "-created_at"
    )

    def get_current_socian(self):
        return self.request.user.socio
    
    def get_queryset(self):
        return SocioPost.objects.filter(
            post_author=self.get_current_socian()
        ).select_related(
            "post_author",
        ).order_by(
            "-created_at"
        )


### ###### ################ #######
## ###### 
## Socio Follow / Unfollow View

class SocioFollowUnfollowView(generics.GenericAPIView):

    throttle_classes = [UserRateThrottle]
    permission_classes = [IsSocian]
    serializer_class = SocioFollowUnfollowSerializer


    # Getting the current logged in Socio User
    def get_current_socian(self):
        return self.request.user.socio
    

    # checking if the given UUID is Valid or NOT
    def is_valid_uuid(self,val):
        try:
            uuid.UUID(str(val))
            return True
        except ValueError:
            return False
        
    
    def post(self,request):
        
        ## Getting the data of id and action
        data = {
        "get_action" : request.POST.get("action_name", None),
        "get_socian_id" : request.POST.get("socio_user_id", None)
        }

        # checking if the given value is UUID or Not
        if not self.is_valid_uuid(data["get_socian_id"]):
            return response.Response({
                "Invalid" : "UUID is Invalid"
            })
        
        # checking if the given socio user id is on database or not
        if not SocioUser.objects.filter(id=data["get_socian_id"]).exists():
            return response.Response({
                "User ID Err" : "Socio User id Not Match"
            })
        
        # initializing the follower and current socio user follower list
        get_socian_follower_id = SocioUser.objects.filter(id=data["get_socian_id"]).first()
        get_current_user_follwers_list = SocioUser.objects.filter(id=self.get_current_socian().id).first()

        if data["get_action"] == "follow":
            if get_current_user_follwers_list.follows.contains(get_socian_follower_id):
                return response.Response({
                    "Exists" : "Sorry The User is already following the Current User"
                })
            
            get_current_user_follwers_list.follows.add(get_socian_follower_id)
            return response.Response({
                "Success" : "Added the follower to current socian follower list"
            })
        
        if data["get_action"] == "unfollow":
            get_current_user_follwers_list.follows.remove(get_socian_follower_id)
            return response.Response({
                "Success" : "Removed the follower from current socian follower list"
            })



