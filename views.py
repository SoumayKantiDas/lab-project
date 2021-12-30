from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    repos=False
    if request.method == 'POST':
        username = request.POST.get('username')
        url = 'https://api.github.com/users/%s/repos' % username
        response = requests.get(url)
        repos = response.json()
    return render(request, 'index.html', context={'repos':repos})

def commit_view(request, user, name, *args, **kwargs):
    repo_name = name
    username = user
    url = 'https://api.github.com/repos/%s/%s/commits' %(username,repo_name)
    response = requests.get(url)
    commits = response.json()
    return render(request, 'commits.html', context={'commits':commits,'repo_name':repo_name,'username':username})

def commit_files_view(request, user, name, ref, *args, **kwargs):
    username = user
    repo_name = name
    refference = ref
    url = 'https://api.github.com/repos/%s/%s/commits/%s' %(username,repo_name,refference)
    response = requests.get(url)
    codes = response.json()
    return render(request, 'File_name.html', context={'codes':codes,'repo_name':repo_name,'username':username,'refference':refference})

def code_view(request, user, name, ref, file, *args, **kwargs):
    username = user
    repo_name = name
    refference = ref
    filename = file.replace("+","/")
    url = "https://github.com/%s/%s/raw/%s/%s" %(username,repo_name,refference,filename)
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    soup_pretty = soup.prettify()
    print(soup_pretty)
    return render(request, 'code.html', context={'soup_pretty':soup_pretty})
