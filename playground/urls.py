# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('hello/', views.say_hello, name='say_hello'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/edit/<int:id>/', views.author_edit, name='author_edit'),
    path('authors/delete/<int:id>/', views.author_delete, name='author_delete'),
]

