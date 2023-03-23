from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.admin import User
import datetime
OrderTypeValue = (("Dining", "Dining"),
                  ("TakeAway", "TakeAway"))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


orderStatusData = (("Pending", "Pending"),
                   ("Delivered", "Delivered"),
                   ("Duplicate", "Duplicate"))


class order(models.Model):
    orderId = models.CharField(max_length=100, primary_key=True)
    orderData = models.TextField()
    orderAmount = models.FloatField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    orderStatus = models.CharField(max_length=100, default="Pending", choices=orderStatusData)

    def __str__(self):
        return str(self.name)


class BookATable(models.Model):
    orderId = models.ForeignKey(order, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    tableNumber = models.IntegerField()
    orderType = models.CharField(max_length=100, default="Dining")

    def __str__(self):
        return str(self.mobile)


class TakeAway(models.Model):
    orderId = models.ForeignKey(order, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    orderType = models.CharField(max_length=100, default="TakeAway")
    address = models.TextField()

    def __str__(self):
        return str(self.mobile)


class Customer(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    email = models.EmailField(blank=True, null=True, default='')
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.mobile)


addressType = (
    ("HOME", "HOME"),
    ("OFFICE", "OFFICE"),
    ("HOTEL", "HOTEL"),
    ("OTHER", "OTHER")
)


class customerAddress(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=10, choices=addressType, default='HOME')
    address_nickname = models.CharField(max_length=100, null=True, default='')
    address = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.address_nickname


class Category(models.Model):
    category_name = models.CharField(max_length=100, primary_key=True)
    image = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    productId = models.CharField(max_length=100, primary_key=True)
    productName = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.TextField()
    halfprice = models.TextField()


class productDetail(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    productFeature = models.TextField()


class SavedCart(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_list = models.TextField()
    cart_ID = models.CharField(max_length=100, primary_key=True)
    status = models.CharField(max_length=1)

    def __str__(self):
        return self.cart_ID


class ReservationTable(models.Model):
    reservationId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    noOfPeople = models.IntegerField()
    date = models.DateField()
    timeSlot = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Pending")
    tableNumber = models.CharField(max_length=100, default="Not Assigned")

    def __str__(self):
        return str(self.mobile)


class ratingdata(models.Model):
    rating = models.IntegerField()
    description = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()

    def __str__(self):
        return str(self.mobile)


orderType = (
    ("TakeAway", "TakeAway"),
    ("Dining", "Dining")
)
paymentType = (
    ("Cash", "Cash"),
    ("Online", "Online"),
    ("Cheque", "Cheque")
)

OrderStatus = (
    ("Pending", "Pending"),
    ("Delivered", "Delivered")

)

class SaleOrder(models.Model):
    orderDataId = models.AutoField(primary_key=True)
    orderId = models.CharField(max_length=100)
    customerName = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    address = models.TextField(null=True)
    orderData = models.TextField()
    orderType = models.CharField(max_length=100, choices=orderType)
    payment = models.CharField(max_length=100, choices=paymentType)
    otherCost = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    cgst = models.CharField(max_length=100)
    sgst = models.CharField(max_length=100)
    Status = models.CharField(max_length=100,choices=OrderStatus,default="Pending")
    datetime = models.DateTimeField(default=datetime.datetime.now())



    def __str__(self):
        return str(self.mobile)

