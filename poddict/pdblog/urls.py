from django.urls import path, include
from pdblog import views
from django.views.generic import TemplateView

app_name = 'pdblog'
urlpatterns = [
        path('', views.ArticleList.as_view(), name='article_list'),
        path('view/<int:article_id>', views.article_view, name='article_view'),
        path('create/', views.ArticleCreate.as_view(), name='article_create'),
        path('edit/<int:pk>', views.ArticleUpdate.as_view(), name='article_update'),
        path('delete/<int:pk>', views.ArticleDelete.as_view(), name='article_delete'),
        path('contact/', views.contactformsend, name='mail_send'),
        path('comment/<int:pk>', views.CommentCreate.as_view(), name='comment_create'),
        path('view/<int:pk>/api/like', views.ArticleLikeApiToggle.as_view(), name='like_api_toggle'),
        path('api-auth/', include('rest_framework.urls')),
        path('tech/', views.TechList.as_view(), name='tech_list'),
        path('poddcast/', views.PodList.as_view(), name='pod_list'),
        path('Notes/', views.NoteList.as_view(), name='note_list'),
        path('about/', TemplateView.as_view(template_name="pdblog/aboutme.html")),

        ]
