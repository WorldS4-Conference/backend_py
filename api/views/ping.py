
# Create your views here.

from rest_framework.decorators import api_view
from django.http import HttpResponse

from api.models import *



@api_view(['GET'])
def ping(request):
    return HttpResponse("API is Live !")

