from django.db import models

# Create your models here.

class Product(models.Model):
    p_name = models.CharField(max_length = 50)
    price = models.IntegerField()
    description = models.TextField(default="")
    quantity = models.IntegerField()
    image = models.ImageField(default = 'abc.jpg', upload_to='Images')
    details = models.TextField(default="")

    class Meta:
        db_table = "Product"


class MyCart(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table ="MyCart"
