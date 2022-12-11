from django.forms import ModelForm
from .models import MessageClient


class MsgForm(ModelForm):
    class Meta:
        model = MessageClient
        fields = ('name_user', 'email_user', 'subject_message', 'message')
        labels = {
            'name_user': 'Ваше имя',
            'email_user': 'Электронная почта',
        }
