from django.contrib import admin
from .models import Article, AllArticles

def publisharticles(modeladmin, request, queryset):
    queryset.update(is_published=True)

publisharticles.short_description = "Publish articles"

def withdrawarticles(modeladmin, request, queryset):
    queryset.update(is_published=False)

withdrawarticles.short_description = "Withdraw articles"

class ArticleAdmin(admin.ModelAdmin):

    fields = ('title', 'text', 'is_published', 'user')
    readonly_fields = ('user',)

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     obj.save()

    list_display = ('title', 'user', 'pub_date', 'is_published')
    list_filter = ('is_published', 'pub_date')
    search_fields = ('title', 'pub_date', 'user', 'text')
    actions = [publisharticles, withdrawarticles]


admin.site.register(AllArticles, ArticleAdmin)
