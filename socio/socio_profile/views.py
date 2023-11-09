
"""
Socio Profile Views 
"""

from rest_framework import generics
from rest_framework.throttling import (
    UserRateThrottle,
    AnonRateThrottle
)
from util_base.utils._permission import IsSocian
from post.models import (
    SocioPost
)
from socio_profile.serialilzers import (
    SocioPostSelfSocianSerializer
)


import logging

logger = logging.getLogger(__name__)


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
