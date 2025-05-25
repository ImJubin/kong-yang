

from .api import fetch_and_save_deposit_products, fetch_and_save_savings_products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DepositProduct, SavingsProduct  # ✅ 또는 SavingsProduct도 같이 필요하면
from .serializers import DepositProductSerializer, SavingsProductSerializer

# @api_view(['GET'])
# def deposit_products_view(request):
#     fetch_and_save_deposit_products()  # API 호출 후 DB 갱신
#     products = DepositProduct.objects.all()
#     serializer = DepositProductSerializer(products, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def savings_products_view(request):
#     fetch_and_save_savings_products()  # API 호출 후 DB 갱신
#     products = DepositProduct.objects.all()
#     serializer = DepositProductSerializer(products, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

from .serializers import DepositProductDetailSerializer, SavingsProductDetailSerializer

@api_view(['GET'])
def deposit_products_view(request):
    fetch_and_save_deposit_products()
    products = DepositProduct.objects.all()
    serializer = DepositProductDetailSerializer(
        products,
        many=True,
        context={'amount': request.query_params.get('amount', 1000000)}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def savings_products_view(request):
    fetch_and_save_savings_products()
    products = SavingsProduct.objects.all()
    serializer = SavingsProductDetailSerializer(
        products,
        many=True,
        context={'amount': request.query_params.get('amount', 1000000)}
    )
    return Response(serializer.data, status=status.HTTP_200_OK)
