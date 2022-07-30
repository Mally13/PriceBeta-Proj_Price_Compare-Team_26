from django.contrib import admin
from .models import Category
from .models import SubCategory
from .models import Product
from .models import Shop
from .models import Sale_Detail
from .models import ProductImage


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','slug','thumbnail')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display =('name', 'category', 'slug')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =('name', 'subcategory', 'brand', 'slug')
    list_filter = ('subcategory','brand')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display =('product','image')
    list_filter = ('product',)

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display =('name',)

@admin.register(Sale_Detail)
class SaleDetailAdmin(admin.ModelAdmin):
    list_display =('product', 'shop', 'price', 'link_to_shop','available')
    list_filter = ('shop','product','available')


