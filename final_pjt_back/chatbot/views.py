from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import openai
from django.contrib import auth
from django.conf import settings
from .models import ChatBot
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from deposits.models import DepositProducts
from finances.models import BankName
import json
import pandas as pd

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')
        user = request.user if request.user.is_authenticated else None

        # 사용자가 입력한 은행 이름을 추출
        bank_name = extract_bank_name(user_message)
        # 해당 은행의 예적금 정보 조회
        products = DepositProducts.objects.filter(kor_co_nm=bank_name)
        if products.exists():
            product_info = "\n".join([
                f"{product.fin_prdt_nm}: {product.spcl_cnd} - {product.join_way} (Max Limit: {product.max_limit or '제한 없음'})"
                for product in products
            ])
            # additional_info.append(product_info)
            additional_info = f"Here are the deposit products for {bank_name}:\n{product_info}"
        else:
            additional_info = f"Sorry, I couldn't find any information for {bank_name}."
        # OpenAI API 호출
        openai.api_key = settings.OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant specialized in providing detailed banking deposit product information based on the given bank name. When the user asks for information about a bank, provide only the specific deposit products, interest rates, joining methods, and maximum limits provided in the additional_info. Do not provide any other information or general descriptions. Tell us these in Korean."},
                {"role": "user", "content": user_message},
                {"role": "system", "content": additional_info}
            ],
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7,
        )
        bot_response = response.choices[0].message['content'].strip()

        # 대화 로그 저장
        chat_log = ChatBot(user=user, message=user_message, response=bot_response)
        chat_log.save()

        return JsonResponse({'response': bot_response})

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def extract_bank_name(user_message):
    banks = BankName.objects.values_list('kor_co_nm', flat=True).distinct()
    for bank_name in banks:
        if bank_name in user_message:
            return bank_name
    return None