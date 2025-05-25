

from .api import fetch_and_save_deposit_products, fetch_and_save_savings_products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DepositProduct, SavingsProduct

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


from rest_framework.generics import RetrieveAPIView
from .models import DepositProduct, SavingsProduct
from .serializers import DepositProductDetailSerializer, SavingsProductDetailSerializer

class DepositProductDetailView(RetrieveAPIView):
    queryset = DepositProduct.objects.all()
    serializer_class = DepositProductDetailSerializer


class SavingsProductDetailView(RetrieveAPIView):
    queryset = SavingsProduct.objects.all()
    serializer_class = SavingsProductDetailSerializer



# views.py
# from openai import OpenAI
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import DepositProduct, SavingsProduct
# from .serializers import DepositProductDetailSerializer, SavingsProductDetailSerializer
# from django.conf import settings

# client = OpenAI(api_key=settings.OPENAI_API_KEY)

# @api_view(['POST'])
# def recommend_products(request):
#     amount = int(request.data.get('amount', 1000000))
    
#     deposits = DepositProduct.objects.all()
#     savings = SavingsProduct.objects.all()

#     deposit_data = DepositProductDetailSerializer(deposits, many=True).data
#     savings_data = SavingsProductDetailSerializer(savings, many=True).data
#     all_data = deposit_data + savings_data

#     prompt = f"""
# 다음은 사용자의 예적금 상품 목록입니다. 
# 금액은 {amount}원이며, 최고 금리를 기준으로 추천 상품 3개를 골라주세요.
# 상품명, 금리, 은행명, 추천 이유를 알려주세요.

# {all_data[:10]}  # 데이터가 너무 크면 일부만 전달
# """

#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=600,
#         temperature=0.7,
#     )

#     return Response({"recommendation": response.choices[0].message.content})
