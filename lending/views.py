from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import MsgForm
from .models import MessageClient


def index(request):
    return render(request, 'lending/index.html')


class MsgCreateView(CreateView):
    # template with form
    template_name = 'index.html'
    # class associated with the model
    form_class = MsgForm
    # address if successful
    success_url = '/'
    success_message = 'Объявление о продаже товара "%(name_user)s" создано.'

