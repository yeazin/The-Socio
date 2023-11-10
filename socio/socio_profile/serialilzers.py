"""

Socio Profile Serializers 

"""

from rest_framework import serializers
from util_base.serializer._initSerializer import TimeStampMixinSerializer
from socio_profile.models import (
    SocioUser,
    SocialLinks
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
## socio Links Serializer

class SocialLinkSerializer(TimeStampMixinSerializer):
    
    social_link_obj_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        model = SocialLinks
        fields = [
            "social_link_obj_id",
            "facebook_url",
            "twitter_url",
            "pinterest_url",
            "tumbler_url",
            "github_url",
            "linkedin_url",
            "instagram_url",
            "discord_url",
            "tiktok_url",
            "thread_url",
            "gravater_url",
            "youtube_url",
            "whatsapp_url",
            "redit_url",
            "skype_url",
            "telegram_url",
            "spotify_url",
            "behance_url",
            "soundcloud_url",
        ]

    
    def create(self, validated_data):

        # getting current logged in socio user
        link_user = self.context["request"].user.socio

        # checking if the current user has already the social links 
        if SocialLinks.objects.filter(socio_user=link_user).exists():
            raise serializers.ValidationError("Sorry ! social Link for this user Already Exists !")
        
        # saving the post with user 
        link_obj = SocialLinks(socio_user=link_user, 
                             **validated_data)
        link_obj.save()

        return link_obj
    

    def update(self, instance, validated_data):

        # Checking the current logged in socio user is the actual author
        link_user = self.context["request"].user.socio
        if not SocialLinks.objects.filter(
            id=instance.id, 
            socio_user=link_user):
            raise serializers.ValidationError("You are not the Actual Author")

        return super().update(instance, validated_data)
    



### #### ##########
## socio profile Serializer

class SocioProfileFuncsSerializer(TimeStampMixinSerializer):

    socio_user_obj_id = serializers.CharField(source="id", read_only=True)

    class Meta:
        model = SocioUser
        fields = [
            "socio_user_obj_id",
            "full_name",
            "profile_image",
            "get_profile_img_url",
            "phone_number",
            "email",
            "bio",
        ]

        read_only_fields = [
            "get_profile_img_url",
        ]


class SocioProfileDetailedSerializer(TimeStampMixinSerializer):

    socio_user_obj_id = serializers.CharField(source="id", read_only=True)
    get_social_links = SocialLinkSerializer(read_only=True)
    total_followers_list = SocioProfileMinifiedserializer(read_only=True,many=True)
    total_followings_list = SocioProfileMinifiedserializer(read_only=True,many=True)


    class Meta:
        model = SocioUser
        fields = [
            "socio_user_obj_id",
            "full_name",
            "get_profile_img_url",
            "phone_number",
            "email",
            "bio",

            "total_followers",
            "total_followers_list",
            "total_followings",
            "total_followings_list",

            "get_total_posts",
            "get_social_links",
        ]

        read_only_fields = [
            "get_profile_img_url",
            "get_total_posts",
            "get_social_links",
        
            "total_followers",
            "total_followers_list",
            "total_followings",
            "total_followings_list",
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

