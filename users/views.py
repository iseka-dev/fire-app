import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required


@require_POST
@csrf_exempt
@login_required
def token_auth(request):
    received_json_data = json.loads(request.body)
    token = received_json_data.get('token')
    get_object_or_404(Token, key=token)
    return JsonResponse({'Response': 'Token valid'})


@require_POST
@csrf_exempt
def user_login(request):
    req = json.loads(request.body)
    password = req.get('password')
    username = req.get('username')
    try:
        username = User.objects.get(username=username)
    except User.DoesNotExist:
        return JsonResponse({'Response': 'User not found'})
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        data = ({'username': user.username, 'token': token.key})
    else:
        data = {'Response': 'Invalid login details supplied.'}
    return JsonResponse(data)


@require_POST
@csrf_exempt
def user_logout(request):
    received_json_data = json.loads(request.body)
    token = received_json_data.get('token')
    user = get_object_or_404(Token, key=token)
    user.delete()
    logout(request)
    return JsonResponse({'Response': 'user logged out'})
