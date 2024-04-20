from django.contrib.auth import get_user_model
from django.db import models

from content.models import Post
from lib.common_models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

User = get_user_model()
class Comment(BaseModel):
    caption = models.TextField(verbose_name=_("caption"), blank=False)
    user = models.ForeignKey(User, verbose_name=_("user"), related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_("post"), related_name='comments', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', related_name="replies", on_delete=models.CASCADE)

    def __str__(self):
        return "user {} comments on post {}".format(self.user.useranme, self.post.id)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class Like(BaseModel):
     user = models.ForeignKey(User, verbose_name=_("user"), related_name='likes', on_delete=models.CASCADE)
     post = models.ForeignKey(Post, verbose_name=_("post"), related_name='likes', on_delete=models.CASCADE)


     class Meta:
         verbose_name = _('comment')
         verbose_name_plural = _('comments')

     def __str__(self):
         return "user {} likes post {}".format(self.user.useranme, self.post.id)
