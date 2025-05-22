

from api import fetch_and_save_deposit_products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def deposit_products_view(request):
    fetch_and_save_deposit_products()  # API 호출 후 DB 갱신
    products = DepositProduct.objects.all()
    serializer = DepositProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)