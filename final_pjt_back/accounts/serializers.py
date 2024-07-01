# accounts/serializers.py
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import User
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    # 필요한 필드들을 추가합니다.
    nickname = serializers.CharField(required=False, max_length=30)
    finance_goal = serializers.CharField(required=False, max_length=100)
    age = serializers.IntegerField(required=False)
    assets = serializers.FloatField(required=False)
    salary = serializers.FloatField(required=False)
    # 해당 필드도 저장 시 함께 사용하도록 설정합니다.
    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = self.validated_data.get('username', '')
        data['password1'] = self.validated_data.get('password1', '')
        data['nickname'] = self.validated_data.get('nickname', '')
        data['finance_goal'] = self.validated_data.get('finance_goal', '')
        data['age'] = self.validated_data.get('age', '')
        data['assets'] = self.validated_data.get('assets', '')
        data['salary'] = self.validated_data.get('salary', '')
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
# UserModel = get_user_model()
# class CustomUserDetailsSerializer(UserDetailsSerializer):
#     class Meta:
#         extra_fields = []
#         if hasattr(UserModel, 'USERNAME_FIELD'):
#             extra_fields.append(UserModel.USERNAME_FIELD)
#         if hasattr(UserModel, 'EMAIL_FIELD'):
#             extra_fields.append(UserModel.EMAIL_FIELD)
#         if hasattr(UserModel, 'first_name'):
#             extra_fields.append('first_name')
#         if hasattr(UserModel, 'last_name'):
#             extra_fields.append('last_name')
#         if hasattr(UserModel, 'nickname'):
#             extra_fields.append('nickname')
#         if hasattr(UserModel, 'finance_goal'):
#             extra_fields.append('finance_goal')
#         if hasattr(UserModel, 'age'):
#             extra_fields.append('age')
#         if hasattr(UserModel, 'assets'):
#             extra_fields.apend('assets')
#         if hasattr(UserModel, 'salary'):
#             extra_fields.append('salary')
#         model = UserModel
#         fields = ('pk', *extra_fields)
#         read_only_fields = ('email',)