from django.contrib import admin
from django.urls import path

from lending.views import index

urlpatterns = [
    # path('message-sent/', message_sent, name='message_sent'),
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
