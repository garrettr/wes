from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models

class ActivePageManager(models.Manager):
    def get_query_set(self):
        return super(ActivePageManager, self).get_query_set().filter(is_active=True).order_by('order_by')

class TopLevelPageManager(models.Manager):
    def get_query_set(self):
        return super(TopLevelPageManager, self).get_query_set().filter(is_toplevel=True).exclude(is_active=False).order_by('order_by')

class Page(models.Model):
    # unique=True?
    url = models.CharField(_('URL'), max_length=100, db_index=True, unique=True)
    title = models.CharField(_('title'), max_length=200)
    #content = models.TextField(_('content'), blank=True)
    content = tinymce_models.HTMLField()
    #enable_comments = models.BooleanField(_('enable comments'))
    template_name = models.CharField(_('template name'), max_length=70, blank=True, help_text=_("Example: 'wes/contact_page.html'. If this isn't provided, the system will use 'wes/default.html'."))
    #sites = models.ManyToManyField(Site)

    # wes features
    is_active = models.BooleanField(_('active'))
    is_toplevel = models.BooleanField(_('top level'))
    order_by = models.IntegerField(default=0, help_text=_("Used to order pages, affects the order they appear in the navigation"))
    sub_pages = models.ManyToManyField('Page', blank=True)

    # Managers
    # Note - the Django admin uses the first manager it sees
    objects = models.Manager()
    active = ActivePageManager()
    toplevel = TopLevelPageManager()

    class Meta:
        ordering = ('url',)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url
