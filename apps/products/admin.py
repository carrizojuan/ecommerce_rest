from django.contrib import admin
from .models import MeasureUnit, Product, CategoryProduct, Indicator
# Register your models here.

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description')

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id','description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator)
admin.site.register(Product, ProductAdmin)