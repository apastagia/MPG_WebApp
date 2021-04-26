from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import joblib


# Create your views here.
reloadModel = joblib.load('./models/RF_MPG.pkl')

def index(request):
    context = {'a':'Hello DjangoFramework'}
    return render(request, 'index.html', context)
    #return HttpResponse({'a':1})

def predictMPG(request):
    print(request)
    if request.method == 'POST':
        temp = {}
        temp['cyl'] = request.POST.get('cylinderVal')
        temp['disp'] = request.POST.get('dispVal')
        temp['hp'] = request.POST.get('hrsPwrVal')
        temp['wt'] = request.POST.get('weightVal')
        temp['acc'] = request.POST.get('accVal')
        temp['yr'] = request.POST.get('modelVal')
        temp['origin'] = request.POST.get('originVal')
    
    testData = pd.DataFrame({'x':temp}).transpose()
    scoreval = reloadModel.predict(testData)[0]
    context = {'scoreval':scoreval}
    return render(request, 'index.html', context)