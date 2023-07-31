from django.contrib import admin

from .models import Article, ArticleCategoryModel, ArticleComment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', 'tag_title', 'slug', 'jpublished', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('tag_title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','url_title', 'jpublished')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'created')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__','article', 'jpublished', 'is_show')
    list_filter = ('created','updated', 'is_show')
    search_fields = ('article', 'fullname')




admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategoryModel, CategoryAdmin)
admin.site.register(ArticleComment, CommentAdmin)

