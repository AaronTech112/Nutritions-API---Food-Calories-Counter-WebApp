from django.shortcuts import render
import requests
import json
# api_key = TQ+Qg+VJubUFEvGh2R6CNg==FihA6K6HupryRo19

# Create your views here.
def home(request):
    if request.method == "POST":
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': 'TQ+Qg+VJubUFEvGh2R6CNg==FihA6K6HupryRo19'})
        if response.status_code == requests.codes.ok:
            return render(request,'FoodieCountApp/home.html',{'api':response.json()})
        else:
            return render(request,'FoodieCountApp/home.html',{'api':'error'})
    else:
        return render(request,'FoodieCountApp/home.html',{'api':'query'})


    