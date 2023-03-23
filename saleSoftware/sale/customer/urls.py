from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("BookATable/",views.BookATableModule.as_view()),
    path('login/', obtain_auth_token, name='login'),
    path('getBookATable/', views.getBookATable.as_view()),

    path("TakeAway/", views.TakeAwayModule.as_view()),
    path('getTakeAway/', views.getTakeAway.as_view()),

    path('calculateBasket/', views.calculateBasket.as_view()),
    path("addingMoreProductData/",views.addingMoreProductData.as_view()),
    path("deleteProductData/",views.deleteProductData.as_view()),

    path('api/getCategory/', views.getCategorys.as_view()),
    path('api/getCategory/<category_name>/', views.getCategorysProduct.as_view()),
    path('api/getAllProduct/', views.getallProduct.as_view()),

    path('getOrderNumber/<number>/', views.getOrderNumber.as_view()),

    path("confirmOrder/",views.confirmOrder.as_view()),
    path("getOrderStatus/<statusData>/",views.getOrderStatus.as_view()),
    path('getDashboardKPIS/',views.getDashboardKPIS.as_view()),

    path('api/postProduct/',views.postProduct.as_view()),

    path('searchFilter/<productName>/', views.searchfilter.as_view()),

    # order
   path('saleOrder/', views.saleOrder.as_view()),
   path('getsaleOrder/', views.getsaleOrder.as_view()),
   path('getSaleOrderData/<Status>/', views.saleOrderData.as_view()),
   path('updateSaleOrderData/', views.updateSaleOrderData.as_view()),
   path('getSaleOrderDate/<Date>/', views.saleOrderDate.as_view()),
   path('saleOrderDateStatus/<Status>/<Date>/', views.saleOrderDateStatus.as_view())

    
]
