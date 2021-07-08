from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name = 'home'),
    path('request', request, name = 'request'),
    path('request/<str:token>', request_check, name = 'request_check'),
    path('sendmail', sendmail, name = 'sendmail'),
]