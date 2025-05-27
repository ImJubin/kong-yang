from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSignupSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

################################## 회원가입 ##################################

@api_view([ 'POST'])
def signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # 프론트에 보낼 회원가입 응답
        return Response({
            "message": "회원가입이 성공적으로 완료되었습니다!",
            "user": {
                    "username": user.username,
            },
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from dj_rest_auth.views import UserDetailsView
from users.serializers import CustomUserDetailsSerializer

class CustomUserDetailsView(UserDetailsView):
    serializer_class = CustomUserDetailsSerializer

print("CustomUserDetailsView serializer:", CustomUserDetailsView.serializer_class)

print("현재 사용 중인 시리얼라이저:", UserDetailsView.serializer_class)


from .models import Account
from .serializers import AccountCreateSerializer, AccountSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_accounts(request):
    if request.method == 'GET':
        accounts = Account.objects.filter(user_id=request.user)
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AccountCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response({"message": "계좌가 추가되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes



@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
def user_accounts_interest(request):
    user = request.user
    accounts = Account.objects.filter(user_id=user)

    # 실시간 이자 갱신
    for account in accounts:
        if hasattr(account, 'savings_detail'):
            account.savings_detail.update_hourly_interest()
        if hasattr(account, 'deposit_detail'):
            account.deposit_detail.update_hourly_interest()

    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SavingsDetail, DepositDetail

@api_view(['GET'])
def calendar_dates(request):
    events = []

    # 적금 시작일 + 만기일
    for sd in SavingsDetail.objects.all():
        events.append({
            'type': '적금 시작',
            'date': str(sd.started_at),
            'name': sd.product_name,
        })
        events.append({
            'type': '적금 만기',
            'date': str(sd.ends_at),
            'name': sd.product_name,
        })

    # 예금 시작일 + 만기일
    for dd in DepositDetail.objects.all():
        events.append({
            'type': '예금 시작',
            'date': str(dd.started_at),
            'name': dd.product_name,
        })
        events.append({
            'type': '예금 만기',
            'date': str(dd.ends_at),
            'name': dd.product_name,
        })

    return Response(events)

from uuid import uuid4
from datetime import date
from dateutil.relativedelta import relativedelta
from decimal import Decimal
from users.models import Account, DepositDetail, SavingsDetail
from fin_products.models import DepositOption, SavingsOption
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import random


def generate_account_number():
    # 12~14자리 숫자 랜덤 생성
    return ''.join([str(random.randint(0, 9)) for _ in range(random.randint(12, 14))])


from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from datetime import date
from dateutil.relativedelta import relativedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import Account, DepositDetail, SavingsDetail
from fin_products.models import DepositOption, SavingsOption
import random



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_product(request):
    user = request.user
    product_type = request.data.get('type')  # 'deposit' or 'savings'
    option_id = request.data.get('option_id')
    amount = Decimal(str(request.data.get('amount', 0)))

    if product_type == 'deposit':
        option = DepositOption.objects.select_related('deposit_product').get(id=option_id)
        product = option.deposit_product

        # 계좌 생성
        acc = Account.objects.create(
            user_id=user,
            bank_name=product.kor_co_nm,
            account_number=generate_account_number(),
            account_type='예금',
            current_balance=amount,
            is_main=False
        )

        # 디테일 붙이기
        DepositDetail.objects.create(
            account=acc,
            product_name=product.fin_prdt_nm,
            interest_rate=option.intr_rate or 0,
            duration_months=option.save_trm,
            started_at=date.today(),
            ends_at=date.today() + relativedelta(months=option.save_trm),
        )


    elif product_type == 'savings':
        from users.models import SavingsPayment  # 납입 모델
        option = SavingsOption.objects.select_related('product').get(id=option_id)
        product = option.product
        duration = option.save_trm
        rate = option.intr_rate or Decimal("0.00")

        # 금액(월 납입액) 검증
        try:
            amount = Decimal(str(request.data.get('amount', '0'))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        except InvalidOperation:
            return Response({'error': '금액이 유효하지 않습니다.'}, status=400)

        # 계좌 생성
        acc = Account.objects.create(
            user_id=user,
            bank_name=product.kor_co_nm,
            account_number=generate_account_number(),
            account_type='적금',
            current_balance=Decimal("0.00"),  # 초기엔 납입 전으로 0원
            is_main=False
        )

        # 목표 금액과 예상 이자 계산
        goal_amount = (amount * duration).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        expected_interest = (
            amount * Decimal(duration + 1) / 2 * (rate / Decimal("100")) * (Decimal("1") / 12)
        ).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

        # 적금 디테일 생성
        savings_detail = SavingsDetail(
            account=acc,
            product_name=product.fin_prdt_nm,
            interest_rate=rate,
            duration_months=duration,
            started_at=date.today(),
            ends_at=date.today() + relativedelta(months=duration),
            total_round=duration,
            goal_amount=goal_amount,
            interest_total=expected_interest 
        )

        # 저장 
        super(SavingsDetail, savings_detail).save()
        savings_detail.update_delay_status()
        savings_detail.save()

        # 1회차 자동 납입 등록
        SavingsPayment.objects.create(
            savings_detail=savings_detail,
            round_number=1,
            paid_at=date.today(),
            amount=amount
        )

        # 계좌 잔액 반영
        acc.current_balance += amount
        acc.save()



    else:
        return Response({'error': '알 수 없는 상품 타입'}, status=400)

    return Response({'message': '계좌 생성 및 상품 가입 완료'})



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_interest(request):
    user = request.user

    updated_accounts = []

    for acc in user.accounts.all():
        if hasattr(acc, 'deposit_detail'):
            acc.deposit_detail.update_hourly_interest()
            updated_accounts.append(f"예금 - {acc.account_number}")

        if hasattr(acc, 'savings_detail'):
            acc.savings_detail.update_hourly_interest()
            updated_accounts.append(f"적금 - {acc.account_number}")

    return Response({
        'message': '이자 업데이트 완료',
        'updated_accounts': updated_accounts
    })




from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountInterestSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_interest_comparison(request):
    accounts = request.user.accounts.all()

    # 금리가 null이 아닌 계좌만 필터링
    filtered_accounts = []
    for acc in accounts:
        rate = None
        if hasattr(acc, 'savings_detail'):
            rate = acc.savings_detail.interest_rate
        elif hasattr(acc, 'deposit_detail'):
            rate = acc.deposit_detail.interest_rate

        if rate is not None:
            filtered_accounts.append(acc)

    serializer = AccountInterestSerializer(filtered_accounts, many=True)
    base_rate = 2.75 # 기준금리

    return Response({
        'base_rate': base_rate,
        'my_accounts': serializer.data
    })








