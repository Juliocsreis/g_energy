# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid


# Create your models here.


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=250)
    phone = models.CharField(blank=True, null=True, max_length=250)
    email = models.CharField(blank=True, null=True, max_length=250)
    created_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class BusinessProposal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True)
    client_id = models.UUIDField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
