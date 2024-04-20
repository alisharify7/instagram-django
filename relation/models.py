from django.contrib.auth import get_user_model
from lib.common_models import BaseModel
from django.db import models


User = get_user_model()
class Relation(BaseModel):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f"{self.from_user.username} Followed {self.to_user.username}"
