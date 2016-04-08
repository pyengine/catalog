import uuid
from django.db import models

class group(models.Model):
    uuid = models.CharField(max_length=20, default='custom_id', help_text='g', unique=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='')
    created = models.DateTimeField(auto_now_add=True, editable=False)

class user(models.Model):
    user_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=20, default='enable')
    email = models.CharField(max_length=255, default='')
    language = models.CharField(max_length=30)
    timezone = models.CharField(max_length=30)
    group = models.ForeignKey('group', to_field='uuid', null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)

class token(models.Model):
    user = models.ForeignKey('user', to_field='user_id')
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)


class portfolio(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024, null=True, blank=True, default=None)
    owner = models.CharField(max_length=20, null=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

class product(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    portfolio = models.ForeignKey('portfolio', to_field='uuid', null=False)
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=1024, null=True, blank=True, default=None)
    description = models.CharField(max_length=5120, null=True, blank=True, default=None)
    provided_by = models.CharField(max_length=100, null=False)
    vendor = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)


