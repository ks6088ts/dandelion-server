from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Category(models.Model):
    category_text = models.CharField(max_length=128)

    def __str__(self):
        return str(self.category_text)


class Brand(models.Model):
    brand_text = models.CharField(max_length=128)

    def __str__(self):
        return str(self.brand_text)


class Product(models.Model):
    product_text = models.CharField(max_length=128)
    measurable_range = models.CharField(max_length=128)
    option = models.CharField(max_length=128)
    serial_number = models.CharField(max_length=32)
    rank = models.CharField(max_length=8)
    year_of_manufacture = models.CharField(max_length=8)

    price = models.IntegerField()

    description = RichTextUploadingField()

    IN_STOCK = "In Stock"
    SOLD = "Sold"
    NEED_TO_CONFIRM = "Need To Confirm"
    INVENTORY_STATUS = (
        (IN_STOCK, IN_STOCK),
        (SOLD, SOLD),
        (NEED_TO_CONFIRM, NEED_TO_CONFIRM),
    )

    inventory_status = models.CharField(
        max_length=128, choices=INVENTORY_STATUS, default=IN_STOCK,
    )

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product_text)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
