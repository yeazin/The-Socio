"""
Post Serializer 
"""

from rest_framework import serializers
from util_base.serializer._initSerializer import TimeStampMixinSerializer
from post.models import (
    SocioPost,
    SocioPostComment,
    BridgeOfPostUserLikes
)


####### ######## ##########
## Minified Version 

class SocioCommentMinifiedSerializer(TimeStampMixinSerializer):

    comment_author = serializers.CharField(source="comment_author.full_name", read_only=True)
    comment_obj_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        model = SocioPostComment
        fields = [
            "comment_obj_id",
            "comment_author",
        ]


###### ####### ####
### Socio Post Serializer

class SocioPostFuncsSerializer(TimeStampMixinSerializer):

    from socio_profile.serialilzers import SocioProfileMinifiedserializer

    get_post_author = SocioProfileMinifiedserializer(read_only=True)
    socio_post_obj_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        model = SocioPost
        fields = [
            "socio_post_obj_id",
            "get_post_author",
            "post_title",
            "post_description",
            "post_image",
            "get_post_img_url"
        ]

        read_only_fields = [
            "socio_post_obj_id",
            "get_post_author",
            "get_post_img_url"
        ]

    
    def create(self, validated_data):

        # getting current logged in socio user
        post_author = self.context["request"].user.socio
        # saving the post with user 
        post_obj = SocioPost(post_author=post_author, **validated_data)
        post_obj.save()

        return post_obj
    

    def update(self, instance, validated_data):

        # Checking the current logged in socio user is the actual author
        post_author = self.context["request"].user.socio
        if not SocioPost.objects.filter(
            id=instance.id, 
            post_author=post_author):
            raise serializers.ValidationError("You are not the Actual Author")

        return super().update(instance, validated_data)
    
 



class SocioPostDetailedSerializer(TimeStampMixinSerializer):
    from socio_profile.serialilzers import SocioProfileMinifiedserializer
    # from post.serializers import SocioCommentMinifiedSerializer

    post_author = SocioProfileMinifiedserializer(read_only=True)
    socio_post_obj_id = serializers.CharField(source="id", read_only=True)
    post_comments = SocioCommentMinifiedSerializer(many=True)

    class Meta:
        model = SocioPost
        fields = [
            "socio_post_obj_id",
            "post_author",
            "post_title",
            "post_description",
            "get_post_img_url",
            "post_comments",
            "total_likes",
            "total_comments",
        ]

        read_only_fields = [
            "socio_post_obj_id",
            "post_author",
            "get_post_img_url",
            "post_comments",
            "total_likes",
            "total_comments",
        ]



###### ####### ####
### Socio Comment Serializer



