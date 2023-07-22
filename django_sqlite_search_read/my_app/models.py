from django.db import models


# Create your models here.

class product_table(models.Model):
    order_date = models.DateField(help_text='Order Date')
    region = models.CharField(max_length=50,help_text='Region')
    city = models.CharField(max_length=50,help_text='City')
    category = models.CharField(max_length=50,help_text='Category')
    product = models.CharField(max_length=50,help_text='Product')
    quantity = models.DecimalField(decimal_places=2,max_digits=18,help_text='Quantity')
    unit_price = models.DecimalField(decimal_places=2,max_digits=18,help_text='Unit Price')

    def __str__(self):
        return self.order_date
