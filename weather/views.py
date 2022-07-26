from django.shortcuts import render
import json 
import urllib.request
def index(request):
    if request.method=='POST':
        city=request.POST['city']
        res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1b9d12f7de1d4a0f7419744a3dd0e036').read()
        json_data=json.loads(res)
        data={
            "country_code":str(json_data['sys']['country']),
            "coordinate":str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
            "temp":str(json_data['main']['temp'])+'k',
            "pressure":str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']),

        }
    else:
        data={}
        city=''
    return render(request,'index.html',{'data':data,'city':city})



# Create your views here.
