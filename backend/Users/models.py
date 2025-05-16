from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # 핸드폰 번호에 대한 정보
    phone_number = models.CharField(max_length=11)

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
