from django.contrib import admin
from .models import Product, Review, Phone, Cultural, Miscellaneous, Section, Cart, ProductsInCart


class ProductsInCartInline(admin.TabularInline):
    model = ProductsInCart
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'price', 'qty', 'release_date', 'status', 'id')
    list_filter = ('section', 'status', 'name', 'release_date')
    search_fields = ('name', 'id')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name', 'id')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Cultural)
class CulturalAdmin(admin.ModelAdmin):
    pass


@admin.register(Miscellaneous)
class MiscellaneousAdmin(admin.ModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'template_name', 'location')
    list_filter = ('name', 'location', 'template_name')
    search_fields = ('name', 'location')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'qty', 'created_at')
    list_filter = ('user', 'created_at')
    inlines = (ProductsInCartInline,)