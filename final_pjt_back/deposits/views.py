from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import requests
from django.http import JsonResponse
from .serializers import DepositProductsSerializer, DepositCartSerializer, DepositOption06Serializer, DepositOption12Serializer, DepositOption24Serializer, DepositOption36Serializer
from .models import DepositProducts, DepositCart, DepositOptions06, DepositOptions12, DepositOptions24, DepositOptions36
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

matplotlib.rcParams['axes.unicode_minus'] = False

matplotlib.rcParams['font.family'] = "AppleGothic"

api_key = '_'

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def save_deposit_prdts(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response['result']['baseList']:
        save_data = {
            'fin_prdt_cd': li.get('fin_prdt_cd'),
            'fin_prdt_nm': li.get('fin_prdt_nm'),
            'kor_co_nm': li.get('kor_co_nm'),
            'dcls_month': li.get('dcls_month'),
            'join_way': li.get('join_way'),
            'mrtr_int': li.get('mrtr_int'),
            'spcl_cnd': li.get('spcl_cnd'),
            'join_deny': li.get('join_deny'),
            'join_member': li.get('join_member'),
            'max_limit': li.get('max_limit'),
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse(response)

@api_view(['GET'])
def deposit_prdts(request):
    products = DepositProducts.objects.all()
    if request.method == 'GET':
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def deposit_cart(request):
    cart = get_list_or_404(DepositCart, user_pk=request.user.id)
    if request.method == 'GET':
        serializer = DepositCartSerializer(cart, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def example(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return Response(response['result']['optionList'])

@api_view(['POST'])
def save_deposit_options(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for li in response['result']['optionList']:
        save_trm = li.get('save_trm')
        if save_trm == '6':
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'save_trm': li.get('save_trm'),
                'intr_rate': li.get('intr_rate'),
                'intr_rate2': li.get('intr_rate2'),
            }
            serializer = DepositOption06Serializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        
        elif save_trm == '12':
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'save_trm': li.get('save_trm'),
                'intr_rate': li.get('intr_rate'),
                'intr_rate2': li.get('intr_rate2'),
            }
            serializer = DepositOption12Serializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        
        elif save_trm == '24':
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'save_trm': li.get('save_trm'),
                'intr_rate': li.get('intr_rate'),
                'intr_rate2': li.get('intr_rate2'),
            }
            serializer = DepositOption24Serializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        
        elif save_trm == '36':
            save_data = {
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'save_trm': li.get('save_trm'),
                'intr_rate': li.get('intr_rate'),
                'intr_rate2': li.get('intr_rate2'),
            }
            serializer = DepositOption36Serializer(data=save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    return JsonResponse(response)

@api_view(['GET'])
def deposit_option_06(request):
    option = DepositOptions06.objects.all()
    if request.method == 'GET':
        serializer = DepositOption06Serializer(option, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def deposit_options(request):
    products = DepositProducts.objects.all()
    pr_serializer = DepositProductsSerializer(products, many=True)
    option_06 = DepositOptions06.objects.all()
    serializer_06 = DepositOption06Serializer(option_06, many=True)
    option_12 = DepositOptions12.objects.all()
    serializer_12 = DepositOption12Serializer(option_12, many=True)
    option_24 = DepositOptions24.objects.all()
    serializer_24 = DepositOption24Serializer(option_24, many=True)
    option_36 = DepositOptions36.objects.all()
    serializer_36 = DepositOption36Serializer(option_36, many=True)

    result = []
    for product in pr_serializer.data:
        res = product
        for option in serializer_06.data:
            if option['fin_prdt_cd'] == product['fin_prdt_cd']:
                res['save_trm_06'] = option['save_trm']
                res['intr_rate_06_1'] = option['intr_rate']
                res['intr_rate_06_2'] = option['intr_rate2']

        for option in serializer_12.data:
            if option['fin_prdt_cd'] == product['fin_prdt_cd']:
                res['save_trm_12'] = option['save_trm']
                res['intr_rate_12_1'] = option['intr_rate']
                res['intr_rate_12_2'] = option['intr_rate2']

        for option in serializer_24.data:
            if option['fin_prdt_cd'] == product['fin_prdt_cd']:
                res['save_trm_24'] = option['save_trm']
                res['intr_rate_24_1'] = option['intr_rate']
                res['intr_rate_24_2'] = option['intr_rate2']

        for option in serializer_36.data:
            if option['fin_prdt_cd'] == product['fin_prdt_cd']:
                res['save_trm_36'] = option['save_trm']
                res['intr_rate_36_1'] = option['intr_rate']
                res['intr_rate_36_2'] = option['intr_rate2']
        if 'save_trm_06' not in res.keys():
            res['save_trm_06'] = 0
            res['intr_rate_06_1'] = 0
            res['intr_rate_06_2'] = 0
        if 'save_trm_12' not in res.keys():
            res['save_trm_12'] = 0
            res['intr_rate_12_1'] = 0
            res['intr_rate_12_2'] = 0
        if 'save_trm_24' not in res.keys():
            res['save_trm_24'] = 0
            res['intr_rate_24_1'] = 0
            res['intr_rate_24_2'] = 0
        if 'save_trm_36' not in res.keys():
            res['save_trm_36'] = 0
            res['intr_rate_36_1'] = 0
            res['intr_rate_36_2'] = 0
        result.append(res)
    return Response(result)

@api_view(['POST', 'DELETE'])
def update_deposit_cart(request, product_pk):
    user = request.user
    product = get_object_or_404(DepositProducts, pk=product_pk)
    if request.method == 'POST':
        cart_item, created = DepositCart.objects.get_or_create(user=user, product=product)
        cart_items = DepositCart.objects.filter(user=user)
        serializer = DepositCartSerializer(cart_items, many=True)
        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Product is already in the cart"}, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        cart_item = get_object_or_404(DepositCart, user=user, product=product)
        cart_item.delete()
        cart_items = DepositCart.objects.filter(user=user)
        serializer = DepositCartSerializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def deposit_cart(request):
    user = request.user
    if request.method == 'GET':
        cart_items = DepositCart.objects.filter(user=user)
        serializer = DepositCartSerializer(cart_items, many=True)
        return Response(serializer.data)

def update_product_rates(product, options, term):
    for option in options:
        if option['fin_prdt_cd'] == product['fin_prdt_cd']:
            product[f'save_trm_{term}'] = option['save_trm']
            product[f'intr_rate_{term}_1'] = option['intr_rate']
            product[f'intr_rate_{term}_2'] = option['intr_rate2']
            break

def create_graph(product):
    terms = [product['save_trm_06'], product['save_trm_12'], product['save_trm_24'], product['save_trm_36']]
    rates_1 = [product['intr_rate_06_1'], product['intr_rate_12_1'], product['intr_rate_24_1'], product['intr_rate_36_1']]
    rates_2 = [product['intr_rate_06_2'], product['intr_rate_12_2'], product['intr_rate_24_2'], product['intr_rate_36_2']]

    terms, rates_1, rates_2 = zip(*((term, rate1, rate2) for term, rate1, rate2 in zip(terms, rates_1, rates_2) if term != 0))

    plt.figure(figsize=(10, 6))
    plt.plot(terms, rates_1, marker='o', label='기본 금리')
    plt.plot(terms, rates_2, marker='o', label='우대 금리')
    plt.title(f"{product['fin_prdt_nm']} ({product['kor_co_nm']})")
    plt.xlabel('예금 기간 (개월)')
    plt.ylabel('이자율 (%)')
    plt.legend()
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close()

    graph = base64.b64encode(image_png).decode('utf-8')
    return {
        'product_name': product['fin_prdt_nm'],
        'bank_name': product['kor_co_nm'],
        'graph': graph
    }

@api_view(['GET'])
def deposit_cart_option(request):
    user = request.user
    if request.method == 'GET':
        cart_items = DepositCart.objects.filter(user=user)
        serializer = DepositCartSerializer(cart_items, many=True)
        option_06 = DepositOptions06.objects.all()
        serializer_06 = DepositOption06Serializer(option_06, many=True)
        option_12 = DepositOptions12.objects.all()
        serializer_12 = DepositOption12Serializer(option_12, many=True)
        option_24 = DepositOptions24.objects.all()
        serializer_24 = DepositOption24Serializer(option_24, many=True)
        option_36 = DepositOptions36.objects.all()
        serializer_36 = DepositOption36Serializer(option_36, many=True)
        graphs = []

        # 각 예금 상품에 대한 이자율 데이터 업데이트
        for product in serializer.data:
            res = product['product']
            update_product_rates(res, serializer_06.data, '06')
            update_product_rates(res, serializer_12.data, '12')
            update_product_rates(res, serializer_24.data, '24')
            update_product_rates(res, serializer_36.data, '36')

            # 기본 값 설정
            default_keys = ['save_trm_06', 'intr_rate_06_1', 'intr_rate_06_2',
                            'save_trm_12', 'intr_rate_12_1', 'intr_rate_12_2',
                            'save_trm_24', 'intr_rate_24_1', 'intr_rate_24_2',
                            'save_trm_36', 'intr_rate_36_1', 'intr_rate_36_2']
            for key in default_keys:
                if key not in res:
                    res[key] = 0
            product['product'] = res

        # 그래프 생성
        for product in serializer.data:
            graph = create_graph(product['product'])
            graphs.append(graph)

        return JsonResponse({'graphs': graphs})



# @api_view(['GET'])
# def deposit_cart_option(request):
#     user = request.user
#     if request.method == 'GET':
#         cart_items = DepositCart.objects.filter(user=user)
#         serializer = DepositCartSerializer(cart_items, many=True)
#         option_06 = DepositOptions06.objects.all()
#         serializer_06 = DepositOption06Serializer(option_06, many=True)
#         option_12 = DepositOptions12.objects.all()
#         serializer_12 = DepositOption12Serializer(option_12, many=True)
#         option_24 = DepositOptions24.objects.all()
#         serializer_24 = DepositOption24Serializer(option_24, many=True)
#         option_36 = DepositOptions36.objects.all()
#         serializer_36 = DepositOption36Serializer(option_36, many=True)
#         graphs = []
#         for product in serializer.data:
#             res = product['product']
#             for option in serializer_06.data:
#                 if option['fin_prdt_cd'] == product['product']['fin_prdt_cd']:
#                     res['save_trm_06'] = option['save_trm']
#                     res['intr_rate_06_1'] = option['intr_rate']
#                     res['intr_rate_06_2'] = option['intr_rate2']
#                     break
#             for option in serializer_12.data:
#                 if option['fin_prdt_cd'] == product['product']['fin_prdt_cd']:
#                     res['save_trm_12'] = option['save_trm']
#                     res['intr_rate_12_1'] = option['intr_rate']
#                     res['intr_rate_12_2'] = option['intr_rate2']
#                     break
#             for option in serializer_24.data:
#                 if option['fin_prdt_cd'] == product['product']['fin_prdt_cd']:
#                     res['save_trm_24'] = option['save_trm']
#                     res['intr_rate_24_1'] = option['intr_rate']
#                     res['intr_rate_24_2'] = option['intr_rate2']
#                     break
#             for option in serializer_36.data:
#                 if option['fin_prdt_cd'] == product['product']['fin_prdt_cd']:
#                     res['save_trm_36'] = option['save_trm']
#                     res['intr_rate_36_1'] = option['intr_rate']
#                     res['intr_rate_36_2'] = option['intr_rate2']
#                     break
#             if 'save_trm_06' not in res.keys():
#                 res['save_trm_06'] = 0
#                 res['intr_rate_06_1'] = 0
#                 res['intr_rate_06_2'] = 0
#             if 'save_trm_12' not in res.keys():
#                 res['save_trm_12'] = 0
#                 res['intr_rate_12_1'] = 0
#                 res['intr_rate_12_2'] = 0
#             if 'save_trm_24' not in res.keys():
#                 res['save_trm_24'] = 0
#                 res['intr_rate_24_1'] = 0
#                 res['intr_rate_24_2'] = 0
#             if 'save_trm_36' not in res.keys():
#                 res['save_trm_36'] = 0
#                 res['intr_rate_36_1'] = 0
#                 res['intr_rate_36_2'] = 0
#             product['product'] = res
        
#         for product in serializer.data:
#             terms = [product['product']['save_trm_06'], product['product']['save_trm_12'], product['product']['save_trm_24'], product['product']['save_trm_36']]
#             rates_1 = [product['product']['intr_rate_06_1'], product['product']['intr_rate_12_1'], product['product']['intr_rate_24_1'], product['product']['intr_rate_36_1']]
#             rates_2 = [product['product']['intr_rate_06_2'], product['product']['intr_rate_12_2'], product['product']['intr_rate_24_2'], product['product']['intr_rate_36_2']]

#             plt.figure(figsize=(10, 6))
#             plt.plot(terms, rates_1, marker='o', label='기본 금리')
#             plt.plot(terms, rates_2, marker='o', label='우대 금리')
#             plt.title(f"{product['product']['fin_prdt_nm']} ({product['product']['kor_co_nm']})")
#             plt.xlabel('예금 기간 (개월)')
#             plt.ylabel('이자율 (%)')
#             plt.legend()
#             plt.grid(True)

#             buffer = BytesIO()
#             plt.savefig(buffer, format='png')
#             buffer.seek(0)
#             image_png = buffer.getvalue()
#             buffer.close()

#             graph = base64.b64encode(image_png).decode('utf-8')
#             graphs.append({
#                 'product_name': product['product']['fin_prdt_nm'],
#                 'bank_name': product['product']['kor_co_nm'],
#                 'graph': graph
#             })

#         plt.clf()
#         return JsonResponse({'graphs': graphs})