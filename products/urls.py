from django.urls import path

from products.views import get_main_view, get_list_view, get_detail_view, get_serarch_view

urlpatterns = [
    path("/main", get_main_view),
    path("/coffee_list", get_list_view),
    path("/coffee/<int:product_id>", get_detail_view),
    path("/search", get_serarch_view)
]