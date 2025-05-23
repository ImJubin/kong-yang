from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # 핸드폰 번호에 대한 정보
    phone_number = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)

class Account(models.Model):
    # 유저와 계좌 정보 1:N으로 연결해주기
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="accounts")
    # 은행
    bank_name = models.CharField(max_length=200)
    # 계좌 번호
    account_number = models.CharField(max_length=200)
    # 계좌 타입
    account_type = models.CharField(max_length=200)
    # 현재 잔액
    current_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    # 메인 계좌 여부
    is_main = models.BooleanField(default=False)
    # 별칭
    alias_name = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 계좌 등록일

    def __str__(self):
        return f"{self.user.username} - {self.account_number}"

# 적금
class SavingsDetail(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='savings_detail')

    product_name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.IntegerField()
    started_at = models.DateField()
    ends_at = models.DateField()
    payment_date = models.DateField()                    # 낸 날짜
    round_number = models.IntegerField()                 # ✅ 납입 회차 정보
    total_round = models.IntegerField()                 # ✅ 전체 납입 회차

    goal_amount = models.DecimalField(max_digits=18, decimal_places=2)  # ✅ 적금 목표 금액



# 예금
class DepositDetail(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='deposit_detail')

    product_name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    duration_months = models.IntegerField()
    started_at = models.DateField()
    ends_at = models.DateField()

