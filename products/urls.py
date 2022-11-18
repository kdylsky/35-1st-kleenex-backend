from django.urls import path

from products.views import ProductDetailView, MainSearchView, get_main_view, get_coffee_list_view

urlpatterns = [
    path('/main/search', MainSearchView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    
    path("/main", get_main_view),
    path("/coffee_list", get_coffee_list_view)
]