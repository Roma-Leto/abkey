from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


from .forms import MsgForm
from .models import MessageClient


def index(request):
    return render(request, 'lending/index.html')


class MsgCreateView(SuccessMessageMixin, CreateView):
    # template with form
    template_name = 'index.html'
    # class associated with the model
    form_class = MsgForm
    # address if successful
    success_url = '/'
    success_message = '"%(name_user)s", Ваше сообщение было отправленно.' \
                      'Мы скоро с Вами свяжемся.'

