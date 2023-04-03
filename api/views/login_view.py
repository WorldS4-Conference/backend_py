from django.shortcuts import render

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password

import os
from PIL import Image
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from api.serializers import UploadedFileSerializer
from api.models import *

@api_view(['POST'])
def login_view(request):

    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user = User.objects.filter(email=email)
        if user.exists() == False:
            return JsonResponse({'message': 'Email Doesnt exists'}, status=404)

        is_password_correct = check_password(password, user[0].password)

        if is_password_correct:
            return JsonResponse({'message': 'Login Successful'}, status=200)
        else:
            return JsonResponse({'message': 'Password Incorrect'}, status=400)
    except Exception as e:
        return JsonResponse({'message': 'Internal Server Error'}, status=500)
