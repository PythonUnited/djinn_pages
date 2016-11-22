from django.core.cache import cache
from django.db import models


class MenuItem(models.Model):

    parent = models.ForeignKey("MenuItem", default=None, null=True, blank=True)
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=256, default="#", null=True, blank=True)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    @property
    def has_sub(self):

        cache_key = "menu-item-%d-has_sub" % self.id
        _has_sub = cache.get(cache_key)

        if _has_sub == None:
            _has_sub = self.menuitem_set.exists()
            cache.set(cache_key, _has_sub)

        return _has_sub

    class Meta:
        ordering = ['order']
