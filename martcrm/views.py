from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    # return redirect('mart-trade/login.html')
    return render(request,'mart-trade/login.html')

def login(request):
    pass
