from wes.models import Page
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe

DEFAULT_TEMPLATE = 'wes/default.html'

def page(request, url):
	"""
	Public interface to the wes Page view
	"""
	if not url.endswith('/') and settings.APPEND_SLASH:
		return HttpResponseRedirect("%s/" % request.path)
	if not url.startswith('/'):
		url = "/" + url
	p = get_object_or_404(Page, url__exact=url, sites__id__exact=settings.SITE_ID)
	return render_page(request, p)

def render_page(request, p):
	"""
	Internal interface to the wes Page view
	"""

	# Load template
	if p.template_name:
		t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
	else:
		t = loader.get_template(DEFAULT_TEMPLATE)

	# Mark title and content as safe - are assumed to be raw HTML content anyway
	# (to avoid having to always use the "|safe" filter in wes templates)
	p.title = mark_safe(p.title)
	p.content = mark_safe(p.content)
	
	c = RequestContext(request, {
		'page': p,
	})		
	response = HttpResponse(t.render(c))
	populate_xheaders(request, response, Page, p.id)
	return response
