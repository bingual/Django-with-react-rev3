from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh, token_verify


urlpatterns = [
    # path('api-token-auth/', obtain_auth_token),
    path('api-simplejwt-auth/', token_obtain_pair),
    path('api-simplejwt-auth/refresh/', token_refresh),
    path('api-simplejwt-auth/verify/', token_verify),
]
