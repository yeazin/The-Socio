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


class SocioPostMinifedSerializer(TimeStampMixinSerializer):

    socio_post_obj_id = serializers.CharField(source="id", read_only=True)
    post_author = serializers.CharField(source="post_author.full_name", read_only=True)

    class Meta:
        model = SocioPost
        fields = [
            "socio_post_obj_id",
            "post_author",
            "post_title"
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
        post_obj = SocioPost(post_author=post_author, 
                             **validated_data)
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


class SocioCommentFuncsSerializer(TimeStampMixinSerializer):

    from socio_profile.serialilzers import SocioProfileMinifiedserializer

    socio_comment_obj_id = serializers.CharField(source="id", read_only=True)
    get_comment_author = SocioProfileMinifiedserializer(read_only=True)
    
    class Meta:
        model = SocioPostComment
        fields = [
            "socio_comment_obj_id",
            "get_comment_author",
            "parent_post",
            "comment"
        ]


    def create(self, validated_data):

        # getting current logged in socio user
        comment_author = self.context["request"].user.socio
        # saving the comment with user 
        comment_obj = SocioPostComment(comment_author=comment_author, 
                                       **validated_data)
        comment_obj.save()

        return comment_obj
    

    def update(self, instance, validated_data):
        # Checking the current logged in socio user is the actual commentor
        comment_author = self.context["request"].user.socio
        if not SocioPost.objects.filter(
            id=instance.id, 
            comment_author=comment_author):
            raise serializers.ValidationError("You are not the Actual Commentor")

        return super().update(instance, validated_data)



###### ####### ####
### Socio Bridge of Likes to Post

class SocioBridgeofPostAndUserSerializer(TimeStampMixinSerializer):

    from socio_profile.serialilzers import SocioProfileMinifiedserializer

    post_bridge_likes_obj_id = serializers.CharField(source="id", read_only=True)
    get_liked_author = SocioProfileMinifiedserializer(read_only=True)
    get_partent_post = SocioPostMinifedSerializer(read_only=True)

    class Meta:
        model = BridgeOfPostUserLikes
        fields = [
            "post_bridge_likes_obj_id",
            "get_liked_author",
            "get_partent_post",
            "liked_author",
            "liked_post"
        ]