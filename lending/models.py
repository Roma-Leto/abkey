from django.db.models import Model, CharField, EmailField, \
    TextField, DateTimeField, BooleanField
from django.contrib.auth.models import AbstractUser


class ABKUsersModel(AbstractUser):
    is_activated = BooleanField(default=True, db_index=True)
    send_message = BooleanField(default=True, verbose_name='Присылать оповещения о новых обращениях')

    class Meta(AbstractUser.Meta):
        pass


class MessageClient(Model):
    name_user = CharField(max_length=50)
    email_user = EmailField()
    subject_message = CharField(max_length=20)
    message = TextField(blank=True, null=True)
    time_send = DateTimeField(auto_now_add=True, db_index=True)
