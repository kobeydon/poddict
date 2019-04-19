from django.urls import path
from pdblog import views

app_name = 'pdblog'
urlpatterns = [
        path('', views.ArticleList.as_view(), name='article_list'),
        path('view/<int:article_id>', views.article_view, name='article_view'),
        path('create/', views.ArticleCreate.as_view(), name='article_create'),
        path('edit/<int:pk>', views.ArticleUpdate.as_view(), name='article_update'),
        path('delete/<int:pk>', views.ArticleDelete.as_view(), name='article_delete'),
        path('contact/', views.contactformsend, name='mail_send')
        ]
