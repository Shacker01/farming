from django.db import models
from django.utils.datetime_safe import datetime
from shop.models.order import order

# Create your models here.


class Client(models.Model):
    First_name = models.CharField(max_length=200)
    Last_name = models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    Email = models.CharField(max_length=20, default=True)
    password1 = models.CharField(max_length=30)
    password2 = models.CharField(max_length=30)

    def __str__(self):
        return self.Username


class Order(order.BaseOrder):
    number = models.PositiveIntegerField("Order Number", null=True, default=None, unique=True)

    def get_or_assign_number(self):
        if self.number is None:
            epoch = datetime.now().date()
            epoch = epoch.replace(epoch.year, 1, 1)
            qs = Order.objects.filter(number__isnull=False, created_at__gt=epoch)
            qs = qs.aggregate(models.Max('number'))
            try:
                epoc_number = int(str(qs['number__max'])[4:]) + 1
                self.number = int('{0}{1:05d}'.format(epoch.year, epoc_number))
            except (KeyError, ValueError):
                # the first order this year
                self.number = int('{0}00001'.format(epoch.year))
        return self.get_number()

    def get_number(self):
        return '{0}-{1}'.format(str(self.number)[:4], str(self.number)[4:])

    @classmethod
    def resolve_number(cls, number):
        number = number[:4] + number[5:]
        return dict(number=number)