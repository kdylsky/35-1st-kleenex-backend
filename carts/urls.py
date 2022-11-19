from django.urls import path

from carts.views import CartAPIView

urlpatterns = [
    path("", CartAPIView.as_view()),
    path("/<int:cart_id>", CartAPIView.as_view())
]