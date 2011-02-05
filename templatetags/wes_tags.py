from django import template
from wes.models import Page

# Compilation function for the get_nav_list template tag
def do_nav_list(parser, token):
    return NavListNode()

class NavListNode(template.Node):
    def render(self, context):
        context['nav_list'] = Page.all()
        return ''
