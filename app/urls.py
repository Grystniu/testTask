from django.contrib import admin
from django.urls import path
from .views import draw_menu, main


urlpatterns = [
    path('', main, name='main_menu'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
