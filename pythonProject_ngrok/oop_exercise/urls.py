from django.urls import path
from . import views

app_name = "oop"

urlpatterns = [
    path("api/orders/json", views.OrdersAPI.as_view(), name="orders_api"),
]
