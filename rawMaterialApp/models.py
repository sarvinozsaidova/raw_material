from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class RawMaterial(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class ProductRawMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class WarehouseBatch(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    remainder = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)