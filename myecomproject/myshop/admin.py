from django.contrib import admin

from myshop.models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','price']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

