from rest_framework import serializers
from .models import DepositOption, DepositProduct, SavingsProduct, SavingsOption




# 예금

# 예금 상품 기본 정보 시리얼라이저
class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'

# 옵션(금리 정보) 시리얼라이저
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'

# 옵션까지 포함한 상세 시리얼라이저
class DepositProductDetailSerializer(serializers.ModelSerializer):
    options = DepositOptionSerializer(many=True, read_only=True)

    class Meta:
        model = DepositProduct
        fields = '__all__'


#########################################################

# 적금


# 금리 옵션 정보
class SavingsOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsOption
        fields = '__all__'

# 적금 기본 정보만 보고 싶을 때
class SavingsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsProduct
        fields = '__all__'

# 옵션까지 포함한 상세 보기 용도
class SavingsProductDetailSerializer(serializers.ModelSerializer):
    options = SavingsOptionSerializer(many=True, read_only=True)

    class Meta:
        model = SavingsProduct
        fields = '__all__'