

"""
Socio Platform 
    Socio User 
"""



from django.db import models
from util_base.models._initModels import TimeStampMixin



class SocioUser(TimeStampMixin):

    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, null=True, 
                                related_name="socio", verbose_name="User", unique=True)
    full_name = models.CharField(max_length=200, null=True, verbose_name="Full Name")
    profile_image = models.ImageField(upload_to='media/socio/', blank=True)
    phone_number = models.CharField(max_length=11, null=True, unique=True, verbose_name="Phone Number")
    email = models.EmailField(max_length=100, unique=True, null=True, verbose_name="Email")


    ## Property of Socio User 

    @property
    def get_profile_img_url(self):
        # returing the absolute image url 
        if self.profile_image and hasattr(self.profile_image, 'url'):
            return self.profile_image.url
        

    @property
    def get_total_posts(self):
        # returning total post count by the socio user
        return self.posts.count()
    
    @property
    def get_social_links(self):
        # returning the social link of socio user
        return self.social_link
    

    def __str__(self) -> str:
        return "Name: {} | Email: {}".format(
            self.full_name,
            self.email
        )
    

    class Meta:
        verbose_name_plural = "Socio Profile"
        indexes = [models.Index(fields=[
            "id", 
            "user",
            "phone_number",
            "email"
            ])]


class SocialLinks(TimeStampMixin):

    socio_user = models.OneToOneField(
            "socio_profile.SocioUser",
            on_delete=models.CASCADE,
            null=True,
            related_name="social_link",
            unique=True,
            verbose_name="Socio User"
        )
    
    facebook_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Facebook Account")
    twitter_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Twitter Account")
    pinterest_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Pinterest Account")
    tumbler_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Tumbler Acount")
    github_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Github Account")
    linkedin_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="LinkedIn Account")
    instagram_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Instagram Account")
    discord_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Discord Account")
    tiktok_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Tiktok Account")
    thread_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Thread Account")
    gravater_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Gravater Account")
    youtube_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Youtube Account")
    whatsapp_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="WhatsApp Account")
    redit_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Redit Account")
    skype_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Skype Account")
    telegram_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Telegram Account")
    spotify_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Spotify Account")
    behance_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="Behance Account")
    soundcloud_url = models.CharField(max_length=200, null=True, blank=True, verbose_name="SoundCloud Account")


    def __str__(self) -> str:
        return "Name : {}".format(
            self.socio_user.__str__()
        )
    
    class Meta:
        verbose_name_plural = "Socio User Social Media Links"
        indexes = [models.Index(fields=[
            "id", 
            "socio_user"
            ])]