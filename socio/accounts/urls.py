
### Accounts Urls 

from django.urls import path
from accounts.views import (
    LoginApiView,
    SocioProfileRegisterView,
    UserChangePasswordView,
    APILogoutView
)


urlpatterns = [
    path('login/', LoginApiView.as_view()),
    path('logout/', APILogoutView.as_view()),
    path('register/', SocioProfileRegisterView.as_view()),
    path('change-password/', UserChangePasswordView.as_view()),
]