from django.contrib import admin
from django.urls import path, include

from lending.views import index, MsgCreateView

urlpatterns = [
    # path('message-sent/', message_sent, name='message_sent'),
    path('', MsgCreateView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
]
