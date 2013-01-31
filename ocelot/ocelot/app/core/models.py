#!/usr/bin/env python
# encoding: utf-8
from django.db import models
from managers import CanceledManager, ActiveManager
from django.utils.translation import ugettext_lazy as _


class DefaultFields(models.Model):
    """
    Class Abstract created date (created_at), updated date (updated_at)
    and active (active)
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))
    active = models.BooleanField(default=True, db_index=True, verbose_name=_('active'))

    objects = models.Manager()
    activeds = ActiveManager()
    canceleds = CanceledManager()

    class Meta:
        abstract = True



class TestDefaultFields(DefaultFields):
    "just for test manager"
    pass
