from django.urls import path, include
from pdblog import views

app_name = 'pdblog'
urlpatterns = [
        path('', views.ArticleList.as_view(), name='article_list'),
        path('view/<int:article_id>', views.article_view, name='article_view'),
        path('create/', views.ArticleCreate.as_view(), name='article_create'),
        path('edit/<int:pk>', views.ArticleUpdate.as_view(), name='article_update'),
        path('delete/<int:pk>', views.ArticleDelete.as_view(), name='article_delete'),
        path('contact/', views.contactformsend, name='mail_send'),
       # path('view/<int:pk>/like', views.ArticleLikeToggle.as_view(), name='like_toggle'),
        path('view/<int:pk>/api/like', views.ArticleLikeApiToggle.as_view(), name='like_api_toggle'),
        path('api-auth/', include('rest_framework.urls'))
        ]
