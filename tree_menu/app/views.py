from django.shortcuts import render
from .models import Menu,MenuItem
# Create your views here.
def index(request):
    return render(request, 'app/base.html', {'menu_list': Menu.objects.all()})


def draw_menu(request, path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('= Draw_menu function failed =')
    print(splitted_path)
    return render(
        request, 'app/base.html',
        {'menu_name': splitted_path[0],
                'menu_item': splitted_path[-1]})