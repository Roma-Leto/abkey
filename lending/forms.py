from django.forms import ModelForm
from .models import MessageClient
from captcha.fields import CaptchaField


class MsgForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = MessageClient
        fields = ('name_user', 'email_user', 'subject_message', 'message')
        labels = {
            'name_user': 'Ваше имя',
            'email_user': 'Ваша электронная почта',
            'subject_message': 'Тема',
            'message': 'Сообщение',
        }
