from django.db import models


class Message(models.Model):
    text = models.CharField(blank=True)
    api = models.CharField(max_length=30, blank=True)
    branch = models.CharField(max_length=30, blank=True)

    @classmethod
    def create(cls, text):
        message = cls(text=text)
        return message
