"""

Socio Profile Serializers 

"""

from rest_framework import serializers
from util_base.serializer._initSerializer import TimeStampMixinSerializer
from socio_profile.models import (
    SocioUser
)


### #### ##########
## Socio Profile 

class SocioProfileMinifiedserializer(TimeStampMixinSerializer):

    socio_user_obj_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        model = SocioUser
        fields = [
            "socio_user_obj_id",
            "full_name"
        ]