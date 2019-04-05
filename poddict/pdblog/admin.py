from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'text' )
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Article, ArticleAdmin)
