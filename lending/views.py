from django.shortcuts import render


def index(request):
    return render(request, 'lending/index.html')


def message_sent(request):
    return render(request, 'lending/msg-sent.html')
