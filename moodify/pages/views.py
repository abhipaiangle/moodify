from django.shortcuts import render
from django.contrib.auth.models import User
import requests
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def get_access_token(request):
    CLIENT_ID = 'a1b9d1bb257b422184ccdf717256c1e0'
    CLIENT_SECRET = '6f3679d7e3bb4591953e0ab88d8cc0c8'
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data['access_token']

    return HttpResponse(f'<h1>{access_token}</h1>')
