from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    # return HttpResponse("계산기 기능 구현 시작입니당")

    # 1. 데이터 확인
    num1 = int(request.GET.get('num1'))
    num2 = int(request.GET.get('num2'))
    operators = request.GET.get('operators')

    # 2. 계산
    if operators == '+':
        result = num1 + num2
    elif operators == '-':
        result = num1 - num2
    elif operators == '*':
        result = num1 * num2
    elif operators == '/':
        result = num1 / num2
    else:
        result = 0
    # 3. 응답

    return render(request, 'calculator.html', {'result': result})