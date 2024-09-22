from django.shortcuts import render
import requests
API_KEY_Ahalya = '03c3cfaed599495a8a6b9c02e2b3baea'
API_KEY_dhilip = '7d07307b1b964bb48e170c60d5b01421'

def home(request):
    country = request.GET.get('country', 'india')
    
    url = f'https://newsapi.org/v2/top-headlines?q={country}&apiKey={API_KEY_dhilip}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    context={
        'articles':articles,
        'country': country 
    }
    return render(request, 'news_api/home.html',context)