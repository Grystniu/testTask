from django.shortcuts import render
from .models import Menu


def main(request):
    return render(request, 'app/main.html', {'menus': Menu.objects.all()})


def draw_menu(request, *args, **kwargs):
    path = kwargs.get('path', None)
    assert path, '= Draw_menu function failed: No path provided ='
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, '= Draw_menu function failed ='
    menu_name = splitted_path[0]
    menu_item = splitted_path[-1]
    return render(request, 'app/main.html', {'menu_name': menu_name, 'menu_item': menu_item})
