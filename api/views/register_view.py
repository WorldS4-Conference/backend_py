
# Create your views here.
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view
from django.http import JsonResponse
from api.models import *


@api_view(['POST'])
def register_view(request):
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user = User.objects.filter(email=email)
        print(user.exists())
        if user.exists():
            return JsonResponse({'message': 'Email already exists'}, status=400)

        user = User(name=name, email=email, password=make_password(password))
        user.save()
        return JsonResponse({'message': 'Registration Successful'}, status=201)

    except Exception as e:
        return JsonResponse({'error': 'Internal Server Error'}, status=500)
