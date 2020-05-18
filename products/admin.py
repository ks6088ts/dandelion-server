from django.contrib import admin

from .models import Brand, Category, Image, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_text",
        "id",
        "price",
        "option",
        "description",
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "id",
        "image",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(Brand)
