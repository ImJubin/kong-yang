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

print("✅ CustomUserDetailsView serializer:", CustomUserDetailsView.serializer_class)

print("📦 현재 사용 중인 시리얼라이저:", UserDetailsView.serializer_class)


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



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def user_accounts(request):
    user = request.user
    accounts = Account.objects.filter(user_id=user)

    # ⏱ 실시간 이자 갱신
    for account in accounts:
        if hasattr(account, 'savings_detail'):
            account.savings_detail.update_hourly_interest()
        if hasattr(account, 'deposit_detail'):
            account.deposit_detail.update_hourly_interest()

    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)







# users/views.py
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




















################################## 로그인 ##################################

# @api_view(['POST'])
# def login(request):
#     serializer = LoginSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.validated_data["user"]

#         # 여기서 토큰 생성 or 조회
#         token, created = Token.objects.get_or_create(user=user)

#         return Response({
#             "message": "로그인 성공!",
#             "user": {
#                 "username": user.username,
#                 "email": user.email,
#             },
#             # 프론트가 저장해서 로그인 상태 유지 가능
#             "token": token.key
#         }, status=status.HTTP_200_OK)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ################################## 로그아웃 ##################################

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout(request):
#     request.user.auth_token.delete()  # ✅ 토큰 삭제
#     return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_200_OK)


# # def logout(request):
# #     auth_logout(request)
# #     return redirect('articles:index')


# ################################## 회원 탈퇴 ##################################

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# # 비활성화 방식의 탈퇴
# def delete_user(request):
#     # 회원 탈퇴시 비밀번호 요구하기
#     password = request.data.get('password')
#     if not password:
#         return Response({"detail": "비밀번호를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)

#     if not request.user.check_password(password):
#         return Response({"detail": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST)

#     request.user.is_active = False
#     request.user.save()

#     # 토큰 삭제
#     Token.objects.filter(user=request.user).delete()
#     return Response({"detail": "회원 탈퇴가 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)



# # def delete(request):
# #     request.user.delete()
# #     return redirect('articles:index')

# ###################################

# def update(request):
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('articles:index')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/update.html', context)


# def change_password(request, user_pk):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)
#             return redirect('articles:index')
#     else:
#         form = PasswordChangeForm(request.user)
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/change_password.html', context)


# def profile(request, username):
#     # username으로 어떤 유저인지 조회
#     # get_user_model().objects.get(username=username)
#     User = get_user_model()
#     person = User.objects.get(username=username)
#     context = {
#         'person': person,
#     }
#     return render(request, 'accounts/profile.html', context)










# def login(request):
#     if request.user.is_authenticated:
#         return redirect('articles:index')

#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('articles:index')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login.html', context)