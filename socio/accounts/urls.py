
### Accounts Urls 

from django.urls import path
from accounts.views import (
    LoginApiView,
    SocioCreateView
)


urlpatterns = [
    path('login/', LoginApiView.as_view()),
    path('register/', SocioCreateView.as_view())
]