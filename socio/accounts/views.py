"""
Accounts Views 

"""
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework import (
    status,
    serializers
)
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import (
    AnonRateThrottle,
    UserRateThrottle
)
from util_base.utils._permission import IsSocian


from accounts.models import User
from socio_profile.models import SocioUser
from accounts.serializers import (
    UserChangePasswordSerializer,
    LoginSerializer,
    CreateProfileSocioSerializer
)


## ####### #######
###### Login View 


class LoginApiView(GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = ()
    UserRateThrottle = [AnonRateThrottle]

    def post(self,request):

        data = {
        "get_identity" : request.POST.get("username"),
        "password" : request.POST.get("password")
        }

        ## checking if ther user exists 
        ## user can input username or phone number
        match_user = User.objects.filter(
            Q(username=data['get_identity'])|
            Q(socio__phone_number=data['get_identity'])|
            Q(socio__email=data['get_identity'])
        ).only(
            'username',
            'socio__phone_number',
            'socio__email'
        )

        # checking if the user found or not
        if match_user.exists():
            user = authenticate(username=match_user.first().username, 
                                password=data['password'])
            if not user:
                raise serializers.ValidationError(
                    {'Error':'Password Mismatch'}
                    )
        else:
            raise serializers.ValidationError(
                {'Error':'User doesn`t exists'}
                )

        # generate token 
        refresh = RefreshToken.for_user(user)

        return Response({
            'access_token':str(refresh.access_token),
            'refresh_token':str(refresh)
        },status=status.HTTP_200_OK)


        
### Socio Profile Register Create View

class SocioProfileRegisterView(generics.CreateAPIView):

    serializer_class = CreateProfileSocioSerializer
    permission_classes = ()
    UserRateThrottle = [AnonRateThrottle]
    queryset = SocioUser.objects.filter()



## Change user password 
## old password, password, confirm password 

class UserChangePasswordView(GenericAPIView):
  throttle_classes = [UserRateThrottle]

  permission_classes = [IsSocian]
  serializer_class = UserChangePasswordSerializer
  
  
  def post(self, request, format=None):
    serializer = UserChangePasswordSerializer(data=request.data, 
                                              context={'user':request.user})
    serializer.is_valid(raise_exception=True)
    return Response({'Message':'Password Changed Successfully'}, 
                    status=status.HTTP_200_OK)
  


# Logout View 

class APILogoutView(GenericAPIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:

            refresh_token = request.data.get('refresh_token')
            token  = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message":"Current user has been Logout"},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":"Invalid Token"})