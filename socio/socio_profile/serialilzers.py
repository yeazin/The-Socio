"""

Socio Profile Serializers 

"""

from rest_framework import serializers
from util_base.serializer._initSerializer import TimeStampMixinSerializer
from socio_profile.models import (
    SocioUser
)


### #### ##########
## Minified Version 

class SocioProfileMinifiedserializer(TimeStampMixinSerializer):

    socio_user_obj_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        model = SocioUser
        fields = [
            "socio_user_obj_id",
            "full_name"
        ]



### #### ##########
## Self post View Serializer 

class SocioPostSelfSocianSerializer(TimeStampMixinSerializer):

    socio_post_obj_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        from post.models import SocioPost

        model = SocioPost
        fields = [
            "socio_post_obj_id",
            "post_title",
            "total_likes",
            "total_comments",
        ] 

        read_only_fields = [
            "socio_post_obj_id",
            "total_likes",
            "total_comments",
        ]

