from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatar/", blank=True, null=True)

    def __str__(self):
        return self.user.username


class Message(BaseModel):
    contact = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="author")

    message = models.TextField(blank=True, null=True)
    voice = models.FileField(verbose_name="voice/", blank=True, null=True)
    image = models.ImageField(upload_to="chat", blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True)

    is_watched = models.BooleanField(default=False)

    def __str__(self):
        return self.contact.user.username


# class Chat(BaseModel):
#     sender = models.ForeignKey(
#         Profile, on_delete=models.CASCADE, related_name="sender")
#     recipient = models.ForeignKey(
#         Profile, on_delete=models.CASCADE, related_name="recipient")

#     message = models.ForeignKey(Message, on_delete=models.CASCADE, blank=True)

#     is_watched = models.BooleanField(default=False)
