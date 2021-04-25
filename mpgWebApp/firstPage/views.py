from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'a':'Hello DjangoFramework'}
    return render(request, 'index.html', context)
    #return HttpResponse({'a':1})

def predictMPG(request):
    print(request)
    if request.method == 'POST':
        print(request.POST.dict())
    context = {'a':'Hello User'}
    return render(request, 'index.html', context)