from django.contrib import admin

from .models import Article


class RelationshipInline(admin.TabularInline):
    model = Article.products.through
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (RelationshipInline,)
    exclude = ['products']
    prepopulated_fields = {'slug': ('title',)}

