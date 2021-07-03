from django.shortcuts import render


@require_POST
@csrf_exempt
def token_auth(request):
    received_json_data = json.loads(request.body)
    token = received_json_data.get('token')
    get_object_or_404(Token, key=token)
    return JsonResponse({'Response': 'Token valid'})


@require_POST
@csrf_exempt
def user_login(request):
    received_json_data = json.loads(request.body)
    token = received_json_data.get('token')
    password = received_json_data.get('password')
    device = received_json_data.get('device')
    try:
        username = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'Response': 'User not found'})
    user_obj = UserProfile.objects.select_related(
        'userpermissions').get(user=username)
    user_role = user_obj.get_user_groups()
    if device == 'desktop' and user_role == {'Seller'}:
        return JsonResponse(
            {'Response': 'You dont have permission to enter the platform.'}
            )
    elif device == 'desktop':
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            data = ({'email': user.email, 'token': token.key})
        else:
            data = {'Response': 'Invalid login details supplied.'}
    elif device == 'mobile':
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            data = {'email': user.email, 'token': token.key}
        else:
            data = {'Response': 'Invalid login details supplied.'}
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
    return JsonResponse({'Response': 'user logged out'})
