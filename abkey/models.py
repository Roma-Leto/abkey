from django.db import models


class Message(models.Model):
    name_user = models.CharField(max_length=50)
    email_user = models.EmailField()
    subject_message = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)
    time_send = models.DateTimeField(auto_now_add=True, db_index=True)
