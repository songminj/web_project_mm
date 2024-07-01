from rest_framework import serializers
from .models import Exchange, BankAddress, BankName

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'

class BankAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAddress
        fields = '__all__'

class BankNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankName
        fields = '__all__'