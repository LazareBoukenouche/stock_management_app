from django.db import models
from django.utils import timezone


# Create your models here.
class Fournisseur(models.Model):
    primary_key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MergedOrder(models.Model):
    primary_key = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date")
    # order_foreign_key = models.ForeignKey('Order', on_delete=models.CASCADE, default=None)
    order = models.ManyToManyField('Order', related_name='orders')

    def __str__(self):
        return self.identifier


class Produit(models.Model):
    KILOGRAMME = 'KG'
    LITER = 'L'
    UNIT = 'U'
    UNIT_CHOICES = [(KILOGRAMME, 'kilogramme'), (LITER, 'Litre'), (UNIT, 'Unitaire')]

    REFRIGERATED_FOOD_ARTICLE = 'alimentaire refrigere'
    DRY_FOOD_ARTICLE = 'alimentaire sec'
    NOT_FOOD_ARTICLE = 'Non alimentaire'
    CATEGORY_CHOICES = [
        (REFRIGERATED_FOOD_ARTICLE, 'alimentaire sec'),
        (DRY_FOOD_ARTICLE, 'alimentaire refrigeres'),
        (NOT_FOOD_ARTICLE, 'Non alimentaire')]

    TAX_CHOICES = [
        (0.055, "5.5"),
        (0.10, "10"),
        (0.20, "20")]

    primary_key = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=100)
    
    article_category = models.CharField(choices=CATEGORY_CHOICES, default=NOT_FOOD_ARTICLE, max_length=100)

    selling_net_price = models.FloatField(max_length=10000, default=0)

    supplier_foreign_key = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, default=None)
    
    current_stock = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    primary_key = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now, verbose_name="Date")
    buying_price_tax_free = models.FloatField(default=0)
    buying_price_full_tax = models.FloatField(default=0)
    supplier_foreign_key = models.ForeignKey('Fournisseur', on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.identifier


class OrderItems(models.Model):
    primary_key = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Produit', on_delete=models.CASCADE)

