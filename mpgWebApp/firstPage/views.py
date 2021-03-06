from django.shortcuts import render
from django.http import HttpResponse

import pandas as pd
import joblib

from pymongo import MongoClient
#client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['mpgDataBase']
collectionD = db['mpgTable']

# Create your views here.
reloadModel = joblib.load('./models/RF_MPG.pkl')

def index(request):
    temp = {}
    temp['cyl'] = 8
    temp['disp'] = 307
    temp['hp'] = 130
    temp['wt'] = 504
    temp['acc'] = 12
    temp['yr'] = 70
    temp['origin'] = 1
    context = {'temp':temp}
    return render(request, 'index.html', context)

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
    context = {'scoreval':scoreval, 'temp':temp}
    return render(request, 'index.html', context)

def viewDatabase(request):
    countOfrow = collectionD.find().count()
    context = {'countOfrow':countOfrow}
    return render(request, 'viewDB.html', context)

def updateDatabase(request):
    temp={}
    temp['cyl']=request.POST.get('cylinderVal')
    temp['disp']=request.POST.get('dispVal')
    temp['hp']=request.POST.get('hrsPwrVal')
    temp['wt']=request.POST.get('weightVal')
    temp['acc']=request.POST.get('accVal')
    temp['yr']=request.POST.get('modelVal')
    temp['origin']=request.POST.get('originVal')
    temp['mpg']=request.POST.get('mpgVal')
    
    collectionD.insert_one(temp)
    countOfrow=collectionD.find().count()

    context={'countOfrow':countOfrow}
    return render(request,'viewDB.html',context)