import datetime
import random
import string
from rest_framework.response import Response
from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework.authtoken.admin import User
from .serializers import *
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework import status
import ast


class BookATableModule(APIView):
    def post(self, request):
        data = request.data
        serializer = BookATableModuleSerializer(data=data)
        if serializer.is_valid():
            mobile = serializer.data["mobile"]
            name = serializer.data["name"]
            email = serializer.data["email"]
            tableNumber = serializer.data["tableNumber"]
            orderAmount = serializer.data["orderAmount"]
            orderData = serializer.data["orderData"]

            try:
                print("Try Block")
                userData = User.objects.filter(username=str(mobile)).values()[0]
                print(userData)
                if userData["username"] == str(mobile):
                    UserId = userData["id"]
                    Username = userData["username"]
                    print(UserId, Username)

                    orderId = 'order' + ''.join(
                        random.choices(string.digits + string.ascii_letters, k=random.randint(10, 14)))

                    order.objects.create(
                        orderId=orderId,
                        orderData=orderData,
                        orderAmount=orderAmount,
                        name_id=UserId
                    )

                    BookATable.objects.create(
                        name=name,
                        mobile=int(Username),
                        email=email,
                        tableNumber=tableNumber,
                        orderId_id=orderId
                    )
            except Exception as e:

                User.objects.create_user(username=str(mobile), password="password", email=email, first_name=name)
                UserData = User.objects.filter(username=str(mobile)).values()[0]
                print("Exception Block", UserData)
                UserId = UserData["id"]
                Username = UserData["username"]
                print(UserId, Username)

                orderId = 'order' + ''.join(
                    random.choices(string.digits + string.ascii_letters, k=random.randint(10, 14)))

                order.objects.create(
                    orderId=orderId,
                    orderData=orderData,
                    orderAmount=orderAmount,
                    name_id=UserId
                )
                BookATable.objects.create(
                    name=name,
                    mobile=int(Username),
                    email=email,
                    tableNumber=tableNumber,
                    orderId_id=orderId
                )
            return Response({
                'status': 200,
                'message': "Dining Order Placed Successfully"
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class getBookATable(APIView):
    def get(self, request, ):
        try:
            data = list(BookATable.objects.filter().values())
            print(data)
            for var in data:
                orderId_id = var["orderId_id"]
                orderData = order.objects.filter(orderId=orderId_id).values()[0]
                namedata = orderData["name_id"]
                username = User.objects.filter(id=namedata).values()[0]["username"]
                var["mobileData"] = int(username)
                var["orderStatus"] = orderData["orderStatus"]
                var["orderDetails"] = ast.literal_eval(orderData["orderData"])
                var["orderAmount"] = orderData["orderAmount"]
            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class TakeAwayModule(APIView):
    def post(self, request):
        data = request.data
        serializer = TakeAwayModuleSerializer(data=data)
        if serializer.is_valid():
            mobile = serializer.data["mobile"]
            name = serializer.data["name"]
            email = serializer.data["email"]
            address = serializer.data["address"]
            orderAmount = serializer.data["orderAmount"]
            orderData = serializer.data["orderData"]

            try:
                userData = User.objects.filter(username=str(mobile)).values()[0]
                if userData["username"] == str(mobile):
                    orderId = 'order' + ''.join(
                        random.choices(string.digits + string.ascii_letters, k=random.randint(10, 14)))

                    UserData = User.objects.filter(username=str(mobile)).values()[0]
                    UserId = UserData["id"]
                    Username = UserData["username"]

                    order.objects.create(
                        orderId=orderId,
                        orderData=orderData,
                        orderAmount=orderAmount,
                        name_id=UserId
                    )

                    TakeAway.objects.create(
                        orderId_id=orderId,
                        name=name,
                        mobile=str(Username),
                        email=email,
                        address=address
                    )

            except Exception as e:

                User.objects.create_user(username=str(mobile), password="password", email=email, first_name=name)
                UserData = User.objects.filter(username=str(mobile)).values()[0]

                UserId = UserData["id"]
                Username = UserData["username"]

                orderId = 'order' + ''.join(
                    random.choices(string.digits + string.ascii_letters, k=random.randint(10, 14)))

                order.objects.create(
                    orderId=orderId,
                    orderData=orderData,
                    orderAmount=orderAmount,
                    name_id=UserId
                )
                TakeAway.objects.create(
                    orderId_id=orderId,
                    name=name,
                    mobile=int(Username),
                    email=email,
                    address=address
                )

            return Response({
                'status': 200,
                'message': "Take Away Order Placed Successfully"
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class getTakeAway(APIView):
    def get(self, request, ):
        try:
            data = list(TakeAway.objects.filter().values())
            print(data)
            for var in data:
                var["address"] = ast.literal_eval(var["address"])
                orderId_id = var["orderId_id"]
                orderId_id = var["orderId_id"]
                orderData = order.objects.filter(orderId=orderId_id).values()[0]
                namedata = orderData["name_id"]
                username = User.objects.filter(id=namedata).values()[0]["username"]
                var["mobileData"] = int(username)
                var["orderStatus"] = orderData["orderStatus"]
                var["orderDetails"] = ast.literal_eval(orderData["orderData"])
                var["orderAmount"] = orderData["orderAmount"]
            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class calculateBasket(APIView):
    def post(self, request):
        data = request.data
        serializer = calculateBasketSerializer(data=data)
        if serializer.is_valid():
            orderData = serializer.data["orderData"]
            result = []
            result2 = []
            try:
                for var in orderData:
                    if var["productId"] not in result:
                        print("IF Block==", var["productId"])
                        result.append(var["productId"])
                    else:
                        print("Else Block==", var["productId"])
                        quantity = var["quantity"]
                        result2.append({var["productId"]: quantity})
                        orderData.remove(var)
                print(result2)
                print(result)
                for var in result2:
                    keyData = list(var.keys())[0]
                    valueData = list(var.values())[0]
                    print(keyData, type(keyData))
                    for var2 in orderData:
                        if keyData == var2["productId"]:
                            print("Match Done!!!")
                            print(var2)
                            var2["quantity"] = var2["quantity"] + valueData
                return Response({
                    'status': 200,
                    'result': orderData
                })
            except Exception as e:
                print(str(e))
            return Response({
                'status': 400,
                'message': "Something Went Wrong Please Try Again"
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class addingMoreProductData(APIView):
    def post(self, request):
        data = request.data
        serializer = addBasketSerializer(data=data)
        if serializer.is_valid():
            orderData = serializer.data["orderData"]
            productId = serializer.data["productId"]
            for var in orderData:
                if var["productId"] == productId:
                    var["quantity"] += 1
            return Response({
                'status': 200,
                'result': orderData
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class deleteProductData(APIView):
    def post(self, request):
        data = request.data
        serializer = addBasketSerializer(data=data)
        if serializer.is_valid():
            orderData = serializer.data["orderData"]
            productId = serializer.data["productId"]
            for var in orderData:
                if var["productId"] == productId:
                    var["quantity"] -= 1
            return Response({
                'status': 200,
                'result': orderData
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class getCategorys(APIView):
    def get(self, request, ):
        try:
            data = list(Category.objects.filter().values())
            print(data)
            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class getCategorysProduct(APIView):
    def get(self, request, category_name):
        try:
            data1 = list(Product.objects.filter(category_name_id=category_name).values())
            print(data1)

            for var in data1:
                del var["category_name_id"]

            return Response({
                'status': 200,
                'data': data1
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class getallProduct(APIView):
    def get(self, request, ):
        try:
            data = list(Product.objects.filter().values())
            print(data)

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class getOrderNumber(APIView):
    def get(self, request, number):
        try:
            UserId = User.objects.filter(username=str(number)).values()[0]["id"]
            data = list(order.objects.filter(name_id=UserId).values())
            print(data)
            for var in data:
                var["orderData"] = ast.literal_eval(var["orderData"])

            return Response({
                'status': 200,
                'data': data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class confirmOrder(APIView):
    def post(self, request):
        data = request.data
        serializer = confirmOrderSerializer(data=data)
        if serializer.is_valid():
            orderStatus = serializer.data['orderStatus']
            orderId = serializer.data["orderId"]
            data = order.objects.filter(orderId=orderId).update(orderStatus=orderStatus)
            print(data)

            return Response({
                'status': 200,
                'message': "Order Updated Successfully"
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'errors': str(e)
        })


class getOrderStatus(APIView):
    def get(self, request, statusData):
        try:
            data = list(order.objects.filter(orderStatus=statusData).values())
            print(data)

            for var2 in data:
                var2["orderData"] = ast.literal_eval(var2["orderData"])
                print("userid==", var2["name_id"])
                username = User.objects.filter(id=var2["name_id"]).values()[0]
                var2["Name"] = username["first_name"]
                var2["mobile"] = username["username"]

            return Response({
                'status': 200,
                'data': data
            })
        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class getDashboardKPIS(APIView):
    def get(self, request):
        try:

            Dashboardata = {}

            Dashboardata["AllOrder"] = len(list(order.objects.filter().values()))
            Dashboardata["CompletedOrder"] = len(list(order.objects.filter(orderStatus="Delivered").values()))
            Dashboardata["PendingOrder"] = len(list(order.objects.filter(orderStatus="Pending").values()))
            Dashboardata["Dining"] = len(list(BookATable.objects.filter().values()))
            Dashboardata["TakeAway"] = len(list(TakeAway.objects.filter().values()))
            # Dashboardata["PendingReservation"]= len(list(ReservationTable.objects.filter(status="Pending").values()))
            return Response({
                'status': 200,
                'data': Dashboardata,
                "message": "Dashboard Details Are"
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class postProduct(APIView):
    def post(self, request):
        try:
            serializer = postProductSerializer(data=request.data)
            if serializer.is_valid():
                Product.objects.create(
                    **serializer.data
                )
                return Response({
                    'status': 200,
                    'data': "Product Added Successfully"
                })
            return JsonResponse({
                'status': 400,
                "Error": "Something Went Wrong",
                "Message": serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class searchfilter(APIView):
    def get(self, request, productName):
        try:

            data = list(Product.objects.filter(productName__icontains=productName).values())
            return JsonResponse({
                'status': 200,
                'data': data,
            })


        except Exception as e:
            print(str(e))
            return JsonResponse({
                'status': 400,
                'message': 'Something Went Wrong',
                'error': str(e)
            })


class saleOrder(APIView):
    def post(self, request):
        data = request.data
        serializer = SaleOrderSerializer(data=data)
        if serializer.is_valid():
            customerName = serializer.data["customerName"]
            orderData = serializer.data["orderData"]
            address = serializer.data["address"]
            orderType = serializer.data["orderType"]
            payment = serializer.data["payment"]
            mobile = serializer.data["mobile"]
            otherCost = serializer.data["otherCost"]
            total = serializer.data["total"]
            cgst = serializer.data["cgst"]
            sgst = serializer.data["sgst"]

            orderId = 'order' + ''.join(
                random.choices(string.digits + string.ascii_letters, k=random.randint(5, 10)))

            SaleOrder.objects.create(
                orderId=orderId,
                customerName=customerName,
                orderData=orderData,
                address=address,
                orderType=orderType,
                payment=payment,
                mobile=mobile,
                otherCost=otherCost,
                total=total,
                cgst=cgst,
                sgst=sgst
            )

            return Response({
                'status': 200,
                'message': "Order  Successfully"
            })
        return Response({
            'status': 400,
            'message': 'Something went wrong',
            'data': serializer.errors
        })


class getsaleOrder(APIView):
    def get(self, request):
        try:
            data = SaleOrder.objects.all().order_by('-orderDataId').values()
            # print(data)

            for var in data:
                var["orderData"] = ast.literal_eval(var["orderData"])

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class saleOrderData(APIView):

    def get(self, request, Status):
        try:
            data = SaleOrder.objects.filter(Status=Status).values()
            print(data)
            for var in data:
                var["orderData"] = ast.literal_eval(var["orderData"])

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class updateSaleOrderData(APIView):
    def post(self, request):
        try:
            serializer = UpdateSaleOrderStatus(data=request.data)
            if serializer.is_valid():
                orderId = serializer.data["orderId"]
                Status = serializer.data["Status"]

                data = SaleOrder.objects.filter(orderId=orderId).update(Status=Status)
                print(data)
                return Response({
                    'status': 200,
                    'data': data
                })
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'Error': str(e)
            })


class saleOrderDate(APIView):

    def get(self, request, Date):
        try:
            data = SaleOrder.objects.filter(Date=Date).values()
            print(data)
            for var in data:
                var["orderData"] = ast.literal_eval(var["orderData"])

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


class saleOrderDateStatus(APIView):

    def get(self, request, Date, Status):
        try:
            data = SaleOrder.objects.filter(Date=Date, Status=Status).values()
            print(data)
            for var in data:
                var["orderData"] = ast.literal_eval(var["orderData"])

            return Response({
                'status': 200,
                'data': data
            })

        except Exception as e:
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'errors': str(e)
            })


from django.shortcuts import render

# Create your views here.
