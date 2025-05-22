# serializers.py
from rest_framework import serializers
from .models import DepositProduct, DepositOption

# 옵션(기간별 금리 정보) 시리얼라이저
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = [
            'save_trm',         # 예치 기간
            'intr_rate',        # 기본 금리
            'intr_rate2',       # 최고 우대 금리
            'intr_rate_type_nm' # 단리/복리
        ]

# 예금 상품 시리얼라이저 (옵션을 포함)
class DepositProductSerializer(serializers.ModelSerializer):
    options = DepositOptionSerializer(many=True, read_only=True)  # 역참조 필드

    class Meta:
        model = DepositProduct
        fields = [
            'id',
            'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm',
            'join_way', 'join_member', 'etc_note',
            'spcl_cnd', 'max_limit', 'dcls_month',
            'created_at',
            'options'
        ]