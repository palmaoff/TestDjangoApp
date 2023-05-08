from django.contrib import admin
from .models import MailList, Client, Message


admin.site.register(MailList)
admin.site.register(Client)
admin.site.register(Message)
