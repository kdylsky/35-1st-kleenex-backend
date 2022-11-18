from django.urls import path

from products.views import MainSearchView, get_main_view, get_list_view, get_detail_view

urlpatterns = [
    path('/main/search', MainSearchView.as_view()),
    path("/main", get_main_view),
    path("/coffee_list", get_list_view),
    path("/coffee/<int:product_id>", get_detail_view),
]