"""
Accounts Views 

"""
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework import (
    status,
    serializers
)
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import (
    AnonRateThrottle,
    UserRateThrottle
)


from accounts.models import User
from accounts.serializers import (
    UserChangePasswordSerializer,
    LoginSerializer
)


## ####### #######
###### Login View 


class LoginApiViews(GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = ()
    # UserRateThrottle = [AnonRateThrottle]

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        
        ## checking if ther user exists 
        ## user can input username or phone number
        match_user = User.objects.filter(
            Q(username=data['username'])
        ).only(
            'username'
        )
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




class LoginApiView(GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = ()
    # UserRateThrottle = [AnonRateThrottle]

    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        match_user = User.objects.filter(
            Q(username=data['username'])
        ).only(
            'username'
        )
        if match_user.exists():
            return Response(
                {"mile": "nai "}
            )
        else:
            return Response({
                "na": "na"
            })