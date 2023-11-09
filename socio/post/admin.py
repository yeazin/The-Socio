from django.contrib import admin
from post.models import (
    SocioPost,
    SocioPostComment,
    BridgeOfPostUserLikes
)


admin.site.register(SocioPost)
admin.site.register(SocioPostComment)
admin.site.register(BridgeOfPostUserLikes)

