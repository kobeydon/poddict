from django.urls import path

from pdblog import views

app_name = 'pdblog'
urlpatterns = [
        path('', views.article_list, name='article_list'),
        path('view/<int:article_id>', views.article_view, name='article_view'),
        # path('new', views.blog_create, name='blog_new'),
        # path('edit/<int:article_id>', views.blog_update, name='blog_edit'),
        # path('delete/<int:article_id>', views.blog_delete, name='blog_delete'),
        ]
