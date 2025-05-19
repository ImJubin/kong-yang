from rest_framework import serializers
from .models import User, Account
from django.contrib.auth import get_user_model
# django의 내장 로그인 기능
from django.contrib.auth import authenticate
# django의 기본 패스워드 검증 도구
from django.contrib.auth.password_validation import validate_password
# 이메일 방지를 위한 검증 도구
from rest_framework.validators import UniqueValidator
#token 모델
from rest_framework.authtoken.models import Token



User = get_user_model()

#############회원가입################
class UserSignupSerializer(serializers.ModelSerializer):
    # 이메일에 대한 중복 검증
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    
    # password = serializers.CharField(write_only=True)
    # password2 = serializers.CharField(write_only=True)

    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password', 'password2')

    # password 1과 2가 둘이 일치하는지 확인
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({ "passwordError": "비밀번호와 비밀번호 확인이 일치하지 않습니다." })
        return data
    
    # 시리얼라이저 내부에 있는 create 오버라이딩
    def create(self, validated_data):
        # 확인용 비번 제거
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(password)
        user.save()
        # 자동 로그인용 token
        # token = Token.objects.create(user=user)
        return user 
    
############# 로그인 #############

class LoginSerializer(serializers.Serializer):
    # 프론트에서 보낸 Json의 username, password, model이 아니어서 meta도 없고 필요없음
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )
        if not user:
            raise serializers.ValidationError({
                "loginError": "아이디 또는 비밀번호가 일치하지 않습니다."
            })
        data["user"] = user
        return data