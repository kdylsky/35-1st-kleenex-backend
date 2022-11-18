from django.http                import JsonResponse

from rest_framework             import status
from rest_framework.parsers     import JSONParser
from rest_framework.decorators  import api_view, parser_classes

from products.service               import ProductService
from decorators.execption_handler   import execption_hanlder

product_service = ProductService()

@execption_hanlder()
@api_view(["GET"])
@parser_classes([JSONParser])
def get_main_view(request, *args, **kwargs):
    return JsonResponse(product_service.get_product_mainpage(), status=status.HTTP_200_OK, safe=False)

@execption_hanlder()
@api_view(["GET"])
@parser_classes([JSONParser])
def get_list_view(request, *args, **kwargs):
    category = request.GET.get('category')
    tastes   = request.GET.getlist('taste')
    sorting  = request.GET.get('sorting')
    offset   = int(request.GET.get('offset', 0))
    limit    = int(request.GET.get('limit', 12))
    return JsonResponse(product_service.get_coffee_list(category, tastes,sorting, offset, limit), status=status.HTTP_200_OK, safe=False)

@execption_hanlder()
@api_view(["GET"])
@parser_classes([JSONParser])
def get_detail_view(request, *args, **kwargs):
    product_id = kwargs["product_id"]
    return JsonResponse(product_service.get_detail(product_id), status=status.HTTP_200_OK)

@execption_hanlder()
@api_view(["GET"])
@parser_classes([JSONParser])
def get_serarch_view(request, *args, **kwargs):
    search = request.GET.get("search")
    return JsonResponse(product_service.get_search(search), status=status.HTTP_200_OK, safe=False)
