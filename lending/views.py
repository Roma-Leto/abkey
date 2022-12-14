from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import MsgForm
from .models import MessageClient

def index(request):
    return render(request, 'lending/index.html')


# class MsgCreateView(CreateView):
#     template_name = 'index.html'
#     form_class = MsgForm
#     success_url = ''

#
# def message_sent(request):
#     # mess = request.POST['message']
#     # print(mess)
#     # if request.method == 'POST':
#     #     msgf = MsgForm(request.POST)
#     #     if msgf.is_valid():
#     #         msgf.save()
#     #         print(msgf.name_user)
#     #     print(dir(msgf))
#     msgf = MsgForm(request.GET)
#     mc = MessageClient(
#         name_user=msgf.name_user,
#         email_user=msgf.email_user,
#         subject_message=msgf.subject_message,
#         message=msgf.message
#     )
#     mc.save()
#     return render(request, 'lending/msg-sent.html')
