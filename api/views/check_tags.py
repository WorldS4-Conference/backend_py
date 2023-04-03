
# Create your views here.

from rest_framework.decorators import api_view
from django.http import HttpResponse
from api.models import *

@api_view(['POST'])
def check_tags(request):
    # data = request.data
    # tags = data.get
    tags = request.POST.getlist('tags')
    print(tags)

    # id_list = [1, 2, 3, 4]

    existing_people = UploadedFile.objects.filter(tag__in=tags)

    return HttpResponse(existing_people.exists())
