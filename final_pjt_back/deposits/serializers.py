from rest_framework import serializers
from .models import DepositProducts, DepositCart, DepositOptions06, DepositOptions12, DepositOptions24, DepositOptions36

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositCartSerializer(serializers.ModelSerializer):
    product = DepositProductsSerializer(read_only=True)
    class Meta:
        model = DepositCart
        fields = ('id', 'product', 'created_at',)

class DepositOption06Serializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions06
        fields = '__all__'

class DepositOption12Serializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions12
        fields = '__all__'

class DepositOption24Serializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions24
        fields = '__all__'

class DepositOption36Serializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions36
        fields = '__all__'