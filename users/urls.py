from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('api/user_login', views.user_login, name='user_login'),
    path('api/user_logout', views.user_logout, name='user_logout'),
    path('api/token_auth', views.token_auth, name='token_auth')
]
