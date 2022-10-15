from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

from Authentication.models import RepeatFields

class Chatting(RepeatFields):
    users = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL , null=True , related_name="chat_user")
    message = RichTextField()