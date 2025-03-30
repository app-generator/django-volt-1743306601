# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    ssh_server = models.CharField(max_length=255, null=True, blank=True)
    ssh_port = models.IntegerField(null=True, blank=True)
    ssh_user = models.CharField(max_length=255, null=True, blank=True)
    ssh_password = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Pdpa Category(models.Model):

    #__Pdpa Category_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    sequence = models.IntegerField(null=True, blank=True)

    #__Pdpa Category_FIELDS__END

    class Meta:
        verbose_name        = _("Pdpa Category")
        verbose_name_plural = _("Pdpa Category")



#__MODELS__END
