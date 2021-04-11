from django.shortcuts import render
from django.http import HttpRequest
from django.shortcuts import render
import requests
def github(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  
        search_result = response.json()
        search_result['success'] = search_was_successful
        search_result['rate'] = {
            'limit': response.headers['X-RateLimit-Limit'],
            'remaining': response.headers['X-RateLimit-Remaining'],
        }
        if 'username' in request.GET:
            username = request.GET['username']
            url = 'https://api.github.com/users/%s/repos' % username
            response = requests.get(url)
            search_was_successful = (response.status_code == 200)  
            search_result = response.json()
    return render(request, 'app/github.html', {'search_result': search_result})
