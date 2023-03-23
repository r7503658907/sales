from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    email = serializers.EmailField(allow_blank=True, allow_null=True, default='')
    password = serializers.CharField(max_length=100)


class CutomerLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100, required=False, allow_blank=True, default='')
    mobile = serializers.CharField(max_length=100, required=False, allow_blank=True, default='')
    password = serializers.CharField(max_length=100)

class postcustomerAddressSerializer(serializers.Serializer):
    address_type = serializers.CharField(max_length=10, default='HOME')
    address_nickname = serializers.CharField(max_length=100, allow_null=True, default='')
    address = serializers.CharField(max_length=100, default='', allow_null=True)


class UpdateAddresserializer(serializers.Serializer):
    address_type = serializers.CharField(max_length=10)
    address_nickname = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)


class AddToCartSerializer(serializers.Serializer):
    product_list = serializers.JSONField()
    mobile = serializers.IntegerField()

class StatusChangeSavecartSerializer(serializers.Serializer):
    savecart_ID = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()

class orderAPISerializer(serializers.Serializer):
    orderData = serializers.JSONField()
    orderAmount = serializers.FloatField()
    mobile = serializers.IntegerField()


class BookATableModuleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    email = serializers.EmailField(required=False,allow_null=True)
    tableNumber = serializers.IntegerField()
    orderData = serializers.JSONField()
    orderAmount = serializers.FloatField()

class TakeAwayModuleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    email = serializers.EmailField(required=False, allow_null=True)
    orderData = serializers.JSONField()
    orderAmount = serializers.FloatField()
    address = serializers.JSONField()


class calculateBasketSerializer(serializers.Serializer):
    orderData= serializers.JSONField()


class addBasketSerializer(serializers.Serializer):
    orderData= serializers.JSONField()
    productId = serializers.CharField(max_length=100)


class bookForReservationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()
    noOfPeople = serializers.IntegerField()
    date = serializers.DateField()
    timeSlot = serializers.CharField(max_length=100)

class UpdateReservationStatusSerializer(serializers.Serializer):
    statusData = serializers.CharField(max_length=100)
    tableNumber = serializers.CharField(max_length=100)
    reservationId = serializers.IntegerField()

class confirmOrderSerializer(serializers.Serializer):
    orderId = serializers.CharField(max_length=100)
    orderStatus = serializers.CharField(max_length=100)

class postRatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField()
    description = serializers.CharField(max_length=500)
    name = serializers.CharField(max_length=100)
    mobile = serializers.IntegerField()


class SaleOrderSerializer(serializers.Serializer):
    customerName = serializers.CharField(max_length=100)
    mobile = serializers.CharField(max_length=100)
    address = serializers.JSONField(required=False,allow_null=True)
    orderData = serializers.JSONField()
    orderType = serializers.CharField(max_length=100)
    payment = serializers.CharField(max_length=100)
    otherCost = serializers.CharField(max_length=100)
    total = serializers.CharField(max_length=100)
    cgst = serializers.CharField(max_length=100)
    sgst = serializers.CharField(max_length=100)


class UpdateSaleOrderStatus(serializers.Serializer):
    orderId = serializers.CharField(max_length=100)
    Status = serializers.CharField(max_length=100)
