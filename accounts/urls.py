from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('api-token-auth/', obtain_auth_token),
    path('api-jwt-auth', obtain_auth_token),
    path('api-jwt-auth/refresh/', obtain_auth_token),
    path('api-jwt-auth/verify', obtain_auth_token),
]