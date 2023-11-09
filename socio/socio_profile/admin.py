from django.contrib import admin
from socio_profile.models import (
    SocioUser,
    SocialLinks
)


admin.site.register(SocioUser)
admin.site.register(SocialLinks)
