from django.core.urlresolvers import reverse
from django.db import models


class Customer(models.Model):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    customer = models.ForeignKey(Customer)
    total = models.IntegerField('Total')

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

    def get_absolute_url(self):
        return reverse('invoicing:invoice_detail', args=(self.pk,))


class Item(models.Model):
    invoice = models.ForeignKey(Invoice)
    title = models.CharField('title', max_length=255)
    quantity = models.DecimalField('quantity', max_digits=10, decimal_places=3, default=1)
    unit_price = models.DecimalField('unit price', max_digits=10, decimal_places=2)

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)

