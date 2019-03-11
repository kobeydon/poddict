from django.urls import path

from pdblog import views

app_name = 'pdblog'
urlpatterns = [
        path('', views.article_list, name='article_list'),
        path('view/<int:article_id>', views.article_view, name='article_view'),
        path('create/', views.article_create, name='article_create'),
        path('edit/<int:article_id>', views.article_update, name='article_update'),
        path('delete/<int:article_id>', views.article_delete, name='article_delete'),
        path('register/', views.writer_create, name='writer_create'),
        path('contact/', views.contactformsend, name='mail_send')
        ]
