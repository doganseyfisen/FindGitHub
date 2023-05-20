from django.shortcuts import render, redirect
import requests
from django.contrib.messages import add_message, WARNING

# Create your views here.

github_url = "https://api.github.com/users/"

def index(request):
    if request.method == 'POST':
        github_username = request.POST.get('githubusername')
        
        response = requests.get(github_url + github_username)
        user_github_info = response.json()
        
        response_repos = requests.get(github_url + github_username + "/repos")
        user_github_repos = response_repos.json()
        
        if "message" in user_github_info:
            add_message(request, WARNING, "There isn't a user has this username.")

            return redirect('index')
        
        else:
            return render(request, 'index.html', {'profile':user_github_info, 'repos':user_github_repos})
            return render(request, 'index.html', {'profile':user_github_info})
    
    else:
        return render(request, 'index.html')
    
