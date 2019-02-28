from django.urls import path

from pdblog import views

urlpatterns = [
        path('', views.blog_list, name='blog_list'),
        path('view/<int:pk>', views.blog_view, name='blog_view'),
        path('new', views.blog_create, name='blog_new'),
        path('edit/<int:pk>', views.blog_update, name='blog_edit'),
        path('delete/<int:pk>', views.blog_delete, name='blog_delete'),
        ]
