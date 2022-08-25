from django.urls import path, include

from rest_framework import urls

urlpatterns =[

    path('', include('dj_rest_auth.urls')),
    path('account/', include('dj_rest_auth.registration.urls')),
 ]