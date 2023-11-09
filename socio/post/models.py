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

    ## Property of Socio Post 

    @property
    def get_socio_post(self):
        return self


    @property
    def get_post_img_url(self):
        if self.post_image and hasattr(self.post_image, 'url'):
            return self.post_image.url
        
    
    @property
    def get_post_author(self):
        return self.post_author


    @property
    def total_likes (self):
        return self.post_likes.count()
    

    @property
    def total_comments(self):
        return self._comments.count()
    
    
    @property
    def post_comments(self):
        return self._comments.select_related(
            "comment_author"
        )
    

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

    
    ## Property of BridgeOfPostUserLikes

    @property
    def get_liked_author(self):
        return self.liked_author
    

    @property
    def get_partent_post(self):
        return self.liked_post

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


    ## Property of Socio Comment

    @property
    def get_comment_author(self):
        # returing the comment author
        return self.comment_author

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
