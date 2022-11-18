from itertools import count
import json
from django.http           import JsonResponse
from django.views          import View
from django.db.models      import Q
from products.models       import Product, ProductImage, TasteByProduct, Grainding, Size
from urllib.parse          import unquote

from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from rest_framework.parsers import JSONParser
from decorators.execption_handler import execption_hanlder
from django.http import JsonResponse
from products.service import ProductService
from products.repository import ProductRepo

product_service = ProductService()

@execption_hanlder()
@api_view(["GET"])
@parser_classes([JSONParser])
def get_main_view(request, *args, **kwargs):
    return JsonResponse(product_service.get_product_mainpage(), status=status.HTTP_200_OK, safe=False)

@execption_hanlder()
@api_view(["GET"])
@parser_classes([JSONParser])
def get_coffee_list_view(request, *args, **kwargs):
    category         = request.GET.get('category')
    tastes           = request.GET.getlist('taste')
    sorting          = request.GET.get('sorting')
    offset           = int(request.GET.get('offset', 0))
    limit            = int(request.GET.get('limit', 12))
    return JsonResponse(product_service.get_coffee_list(category, tastes,sorting, offset, limit), status=status.HTTP_200_OK, safe=False)


class ProductDetailView(View): 
    def get(self, request, product_id): 
        try:

            product        = Product.objects.get(id=product_id)

            product_detail = (
                {
                    'id'               : product.id,
                    'name'             : product.name,
                    'price'            : product.price,
                    'img'              : [{
                        'img_id'       : image.id,
                        'img_url'      : image.url
                    } for image in product.productimage_set.all()],

                    'taste'            : [{
                        'taste_id'     : flavor.taste.id,
                        'taste_name'   : flavor.taste.name
                    } for flavor in product.tastebyproduct_set.all()],
                    'graind'           : [{
                        'graind_id'    : graind.id,
                        'graind_type'  : graind.type
                    } for graind in product.grainding_set.all()],
                    'size'             : [{
                        'size_id'      : size.id,
                        'size_name'    : size.name,
                        'size_price'   : size.price
                    } for size in product.size_set.all()],
                }
            )
            return JsonResponse({'product_detail' : product_detail}, status = 200)

        except Product.DoesNotExist:
            return JsonResponse({'MESSAGE' : 'Product matching query does not exist.'}, status = 404)


class MainSearchView(View):
    def get(self, request):
        search = request.GET.get('keywords')
        products = Product.objects.filter(name__icontains=unquote(search))

        result = [{  
                    'id'             : product.id,
                    'name'           : product.name,
                    'eng_name'       : product.eng_name,
                    'img'            : [{
                        'img_id'     : image.id,
                        'img_url'    : image.url
                    } for image in product.productimage_set.all()],
                    'taste'          : [{
                        'taste_id'   : flavor.taste.id,
                        'taste_name' : flavor.taste.name
                    } for flavor in product.tastebyproduct_set.all()],
                    'roasting_date'  : product.roasting_date,
                    'price'          : product.price
                }for product in products]

        if len(products) == 0:
            return JsonResponse({'MESSAGE' : 'NO RESULT'}, status=404)

        return JsonResponse({'result' : result}, status =200)


class MainSearchView(View):
    def get(self, request):
        search   = request.GET.get('keywords')
        products = Product.objects.filter(name__icontains=unquote(search))

        result = [{  
                    'id'             : product.id,
                    'name'           : product.name,
                    'eng_name'       : product.eng_name,
                    'img'            : [{
                        'img_id'     : image.id,
                        'img_url'    : image.url
                    } for image in product.productimage_set.all()],
                    'taste'          : [{
                        'taste_id'   : flavor.taste.id,
                        'taste_name' : flavor.taste.name
                    } for flavor in product.tastebyproduct_set.all()],
                    'roasting_date'  : product.roasting_date,
                    'price'          : product.price
                }for product in products]

        if not products.exists():
            return JsonResponse({'MESSAGE' : 'NO RESULT'}, status=404)

        return JsonResponse({'result' : result}, status =200)