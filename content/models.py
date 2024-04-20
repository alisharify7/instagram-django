from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import gettext_lazy as _

from location.models import Location

# Create your models here.


User = get_user_model()
class Post(BaseModel):
    caption = models.TextField(_('caption'), blank=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='posts', on_delete=models.CASCADE)
    media = models.ForeignKey('Media', related_name='posts', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return f"{self.id} -> {self.user.username}"


class Media(BaseModel):
    IMAGE = 0
    VIDEO = 1

    MEDIA_TYPE_CHOICES = (
        (IMAGE, _("Image")),
        (VIDEO, _("Video")),
    )

    type = models.PositiveSmallIntegerField(choices=MEDIA_TYPE_CHOICES, verbose_name=_('media type'), default=IMAGE)
    hash_value = models.TextField(_('hash value'), blank=True)
    media_file = models.FileField(_('media file'), upload_to='content/media/', validators=[
        FileExtensionValidator(allowed_extensions=("png", 'jpg', 'jpeg', 'gif', 'webp'))
    ]) # need a validator


    def __str__(self):
        return f"{self.id}-{self.media_file}"


class Tag(BaseModel):
    title = models.CharField(_('title'), max_length=32)

    def __str__(self):
        return self.title

class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name='hashtag', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return "post {} has tag id {}".format(self.post.id, self.tag.title)



class TaggedUser(BaseModel):
    post = models.ForeignKey(Post, related_name='tagged_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='tagged_posts', on_delete=models.CASCADE)

    def __str__(self):
        return "{} tagged in post {}".format(self.user.username, self.post.id)