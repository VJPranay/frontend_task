from django.contrib import admin
from .models import Category, ProductImage, Product, ProductReview

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty forms to display

class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1  # Number of empty forms to display

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'description', 'price', 'stock')
    inlines = [ProductImageInline, ProductReviewInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'review', 'rating')
