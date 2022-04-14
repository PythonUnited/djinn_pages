from djinn_pages.models.menu import MenuItem
from django.template import Library

register = Library()

@register.inclusion_tag('djinn_pages/snippets/menuitem.html', takes_context=True)
def custommenu(context, parent=None):
    """
    DEPRECATED
    """
    menuitems = MenuItem.objects.filter(parent = parent)

    context.update({'menuitems': menuitems})
    return context

@register.inclusion_tag('gronet_v3/includes/menuitem.html', takes_context=True)
def custommenu_v3(context, parent=None):

    menuitems = MenuItem.objects.filter(parent = parent)

    context.update({'menuitems': menuitems})
    return context
