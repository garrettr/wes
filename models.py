from django.db import models
from django.contrib.site.models import Site
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
	# unique=True?
	url = models.CharField(_('URL'), max_length=100, db_index=True)
	title = models.CharField(_('title'), max_length=200)
	content = models.TextField(_('content'), blank=True)
	enable_comments = models.BooleanField(_('enable comments'))
	template_name = models.CharField(_('template name'), max_length=70, blank=True, help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
	sites = models.ManyToManyField(Site)

	# wes features
	is_draft = models.BooleanField(_('draft'))
	sub_pages = models.ManyToManyField(Page)
	# show_after = models.ForeignKey('Page', null=True, blank=True, default=None, related_name="flatpage_parent", help_text="Page that this one should after after (if any)")

	class Meta:
		ordering = ('url',)

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)

	def get_absolute_url(self):
		return self.url
