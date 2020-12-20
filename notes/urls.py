from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add"),
    path('add2', views.add2, name="add2"),
    path('entry/<int:id>', views.entry, name='entry'),
    path('tag/<str:tag>', views.tag, name='tag'),
]
