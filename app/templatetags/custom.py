from django.core.cache import cache
from django.db.models import Prefetch
from app.models import MenuItem, Menu
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('app/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):

    def get_menu(menu_item: str = None, sub_menu: list = None):
        menu = []
        if menu_item is None:
            menu = list(items.filter(parent=None))
        else:
            menu = list(items.filter(parent__name=menu_item))
        try:
            menu.insert(menu.index(sub_menu[0].parent) + 1, sub_menu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(name=menu_item).parent.name, menu)
        except AttributeError:
            return get_menu(sub_menu=menu)
        except ObjectDoesNotExist:
            return menu

    items = MenuItem.objects.filter(menu__name=menu_name)

    if menu_name == menu_item:
        method = get_menu()
    else:
        method = get_menu(menu_item)

    return {'menu': method}
