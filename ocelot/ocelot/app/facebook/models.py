from django.utils.translation import ugettext as _
from django.db import models

from ocelot.app.core.models import DefaultFields



class Campaign(DefaultFields):
    facebook_id = models.BigIntegerField(verbose_name=_('facebook id'))
    likers = models.ManyToManyField('fandjango.User', through='Like', related_name='Campaigns')
    owner = models.ForeignKey('fandjango.User', related_name=_('owner'))

    class Meta:
        verbose_name = _('Campaign')
        verbose_name_plural = _('Campaigns')

    def __unicode__(self):
        pass


class Like(DefaultFields):
    campaign = models.ForeignKey('Campaign', verbose_name=_('campaign'))
    facebook_user = models.ForeignKey('fandjango.User', verbose_name=_('facebook user'))

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')

    def __unicode__(self):
        pass
