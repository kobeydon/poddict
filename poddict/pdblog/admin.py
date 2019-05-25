from django.contrib import admin
from .models import Article, AllArticles, Comment, AllComments

def publish(modeladmin, request, queryset):
    queryset.update(is_published=True)

publish.short_description = "Publish"

def withdraw(modeladmin, request, queryset):
    queryset.update(is_published=False)

withdraw.short_description = "Withdraw"

class ArticleAdmin(admin.ModelAdmin):

    fields = ('title', 'text', 'is_published', 'user', 'likes')
    readonly_fields = ('user',)

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()

    list_display = ('title', 'user', 'pub_date', 'is_published' )
    list_filter = ('is_published', 'pub_date')
    search_fields = ('title', 'pub_date', 'user', 'text')
    actions = [publish, withdraw]

class CommentAdmin(admin.ModelAdmin):
    
    actions = [publish, withdraw]
    list_display = ('comment_text', 'is_published')

admin.site.register(AllArticles, ArticleAdmin)
admin.site.register(AllComments, CommentAdmin)
