"""
Post database file 

"""
from django.db import models
from util_base.models._initModels import TimeStampMixin


## ## ####
## Socio Post model 

class SocioPost(TimeStampMixin):

    post_author = models.ForeignKey(
        "socio_profile.SocioUser",
        on_delete=models.CASCADE,
        null=True,
        related_name="posts",
        verbose_name="Post Author"
    )
    post_title = models.CharField(max_length=200, null=True, verbose_name="Post Title")
    post_description = models.TextField(null=True, blank=True, verbose_name="Post Details")
    post_image = models.ImageField(upload_to='media/post/', blank=True)
    post_likes = models.ManyToManyField("socio_profile.SocioUser", 
                                        through="BridgeOfPostUserLikes",
                                        related_name="liked_post")


    def __str__(self) -> str:
        return "Title : {}".format(
            self.post_title
        )
    

    class Meta:
        verbose_name_plural = "Socio Post Archive"
        indexes = [models.Index(fields=[
            "id", 
            "post_author",
            "post_title",
            ])]



## ## ####
## Socio Post & User likes model 

class BridgeOfPostUserLikes(TimeStampMixin):

    liked_author = models.ForeignKey(
        "socio_profile.SocioUser",
        on_delete=models.CASCADE,
        null=True,
        related_name="liked_post_bridge",
        verbose_name="Liked Author"
    )
    liked_post = models.ForeignKey(
        "post.SocioPost",
        on_delete=models.CASCADE,
        null=True,
        related_name="_liked_bridge",
        verbose_name="Liked Post"
    )

    
    def __str__(self) -> str:
        return "Post : {} | Author : {}".format(
            self.liked_post.__str__(),
            self.liked_author.__str__()
        )
    
    class Meta:
        verbose_name_plural = "Socio Post Liked Archive"
        indexes = [models.Index(fields=[
            "id", 
            "liked_author",
            "liked_post",
            ])]
        unique_together = (
            "liked_author",
            "liked_post",
        )



## ## ####
## Socio Post Comment model 

class SocioPostComment(TimeStampMixin):

    comment_author = models.ForeignKey(
        "socio_profile.SocioUser",
        on_delete=models.CASCADE,
        null=True,
        related_name="posted_comments",
        verbose_name="Comment Author"
    )
    parent_post = models.ForeignKey(
        "post.SocioPost",
        on_delete=models.CASCADE,
        null=True,
        related_name="_comments"
    )
    comment = models.CharField(max_length=200, null=True, verbose_name="Comment")


    def __str__(self) -> str:
        return "Post : {} | Author : {}".format(
            self.parent_post.__str__(),
            self.comment_author.__str__()
        )


    class Meta:
        verbose_name_plural = "Socio Post Comment Archive"
        indexes = [models.Index(fields=[
            "id", 
            "comment_author",
            "parent_post",
            ])]
        unique_together = (
            "comment_author",
            "parent_post",
        )
