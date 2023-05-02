from django.db import models
from rest_framework import serializers
# Create your models here.


class Nou(models.Model):
    name = models.CharField(max_length=50, help_text="اسم محصول", unique=True)
    price = models.IntegerField(help_text="قیمت محصول")

    def __str__(self):
        return self.name


class Product(models.Model):
    nou = models.ForeignKey(
        Nou,
        on_delete=models.CASCADE,
        related_name="nou",
        help_text="نوع محصول"
    )

    count = models.IntegerField(help_text="تعداد ")
    submitdate = models.IntegerField(help_text="تاریخ ثبت محصول")

    def __str__(self):
        return self.nou.name


class NouSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nou
        fields = ['name', 'price']


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['count', 'submitdate']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data['name'] = instance.nou.name
        data['price'] = instance.nou.price

        return data
