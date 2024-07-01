from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from django.http import JsonResponse
from .serializers import ExchangeSerializer, BankAddressSerializer, BankNameSerializer
import pandas as pd
from .models import BankName, Exchange, BankAddress


api_key_ex = '_'
api_key_de = '_'

@api_view(['POST'])
def save_exchange_rate(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={api_key_ex}&data=AP01'
    response = requests.get(url).json()
    for li in response:
        save_data = {
            'cur_unit': li.get('cur_unit'),
            'cur_nm': li.get('cur_nm'),
            'tts': li.get('tts'),
            'deal_bas_r': li.get('deal_bas_r'),
        }
        serializer = ExchangeSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse(response, safe=False)

@api_view(['GET'])
def exchange_rate(request):
    exchange = Exchange.objects.all()
    if request.method == 'GET':
        serializer = ExchangeSerializer(exchange, many=True)
        return JsonResponse(serializer.data, safe=False)


df = pd.read_csv('assets/시도명시군구_240513.csv', encoding='utf-8')
def save_address(request):
    data = df.to_dict('records')
    for li in data:
        save_data = {
            'sido': li.get('시도명'),
            'sigungu': li.get('시군구명')
        }
        serializer = BankAddressSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse(data)

@api_view(['GET'])
def address(request):
    address_data = BankAddress.objects.order_by('sido', 'sigungu')
    if request.method == 'GET':
        serializer = BankAddressSerializer(address_data, many=True)
        return JsonResponse(serializer.data, safe=False)

def save_bank(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key_de}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response['result']['baseList']:
        save_data = {
            'kor_co_nm': li.get('kor_co_nm'),
        }

        serializer = BankNameSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse(response)

@api_view(['GET'])
def bank(request):
    banks = BankName.objects.distinct().order_by('kor_co_nm')
    if request.method == 'GET':
        serializer = BankNameSerializer(banks, many=True)
        res = []
        bankname = set()
        for bank in serializer.data:
            if bank['kor_co_nm'] not in bankname:
                bankname.add(bank['kor_co_nm'])
                res.append(bank)
        return Response(res)