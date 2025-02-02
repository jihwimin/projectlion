from django.shortcuts import render

# Create your views here.
def inputLength(request):
    result = 0
    string1 = request.GET.get('string1')
    result = len(string1)
    return render(request, 'inputLength.html', {'result': result})

def wonToDollars(request):
    won = request.GET.get('inputWon')
    dollar = request.GET.get('inputDollar')
    mode = request.GET.get('mode')
    if mode == 'dollar' :
        result = int(won) * 0.00069
    elif mode == 'won':
        result = int(dollar) * 1,457.78
    else:
        result = 0
    
    return render(request, 'wonToDollars.html', {"result": result})
