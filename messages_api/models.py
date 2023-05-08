from django.db import models
from django.utils import timezone


class MailList(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    text = models.TextField(default='')
    mobile_code_filter = models.CharField(max_length=10, blank=True)
    tag_filter = models.CharField(max_length=50, blank=True)


class Client(models.Model):
    number = models.CharField(max_length=11, blank=True)
    mobile_code = models.CharField(max_length=10, blank=True)
    tag = models.CharField(max_length=50, blank=True)
    time_zone = models.CharField(max_length=50, blank=True)


class MessageStatus(models.TextChoices):
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    WAIT = 'WAIT'


class Message(models.Model):
    send_time = models.DateTimeField(blank=True, default=timezone.now)
    status = models.CharField(
        max_length=20,
        choices=MessageStatus.choices,
        default=MessageStatus.WAIT,
    )
    mail_list = models.ForeignKey(MailList, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
