from django.urls import path

from carts.views import CartView, CartAPIView

urlpatterns = [
    path('/cart', CartView.as_view()),
    path("/test", CartAPIView.as_view())
]