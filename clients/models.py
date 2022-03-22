from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=250, blank=True, null=True)
    msg = models.CharField(max_length=250, blank=True, null=True)
    created = models.DateTimeField(null=True, blank=True, auto_created=True)
    lead_origin = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.pk, self.email)