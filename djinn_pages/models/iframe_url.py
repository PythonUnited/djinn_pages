from django.utils.translation import gettext_lazy as _
from django.db import models


class AllowedIFrameURL(models.Model):

    url_name = models.SlugField(
        max_length=100,
        unique=True,
        help_text=_('Wordt gebruikt om de link naar de iframe-pagina te '
                    'maken. Alleen letters, cijfers, liggende streepjes en '
                    'verbindingsstreepjes toegestaan.'))

    url = models.TextField(
        max_length=1024)

    class Meta:
        verbose_name = _('Allowed IFrame URL')
        verbose_name_plural = _('Allowed IFrame URLs')
        ordering = ['url_name']
