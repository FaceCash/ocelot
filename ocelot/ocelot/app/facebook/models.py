from django.utils.translation import ugettext as _
from django.db import models

from ocelot.app.core.models import DefaultFields



class Campaign(DefaultFields):
    title = models.CharField(max_length=300, default='Title', verbose_name=_('title'))
    facebook_id = models.BigIntegerField(verbose_name=_('facebook id'))
    likers = models.ManyToManyField('fandjango.User', through='Like', related_name='Campaigns')
    owner = models.ForeignKey('fandjango.User', related_name=_('owner'))
    price = models.ForeignKey('Price', verbose_name=_('price'))
    limit_likes = models.IntegerField(default=100, verbose_name=_('limit of likes'))

    class Meta:
        verbose_name = _('Campaign')
        verbose_name_plural = _('Campaigns')

    def __unicode__(self):
        return 'Owner: %s | Title: %s' % self.owner.username, self.title

    @property
    def likes_count(self):
        return self.likes.all().count()



class Like(DefaultFields):
    campaign = models.ForeignKey('Campaign', verbose_name=_('campaign'), related_name='likes')
    facebook_user = models.ForeignKey('fandjango.User', verbose_name=_('facebook user'), related_name='likes')

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')
        unique_together = (('campaign', 'facebook_user'),)

    def __unicode__(self):
        return 'Campaign: %s. Username: %s' % (self.campaign.title, self.facebook_user.username)


class Price(DefaultFields):
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name=_('total'))
    user_commission = models.DecimalField(max_digits=7, decimal_places=2, default=0.00, verbose_name=_('user cost'))

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')

    def __unicode__(self):
        return 'Total: $%s | User commission: $%s' % (str(self.total), str(self.user_commission))




