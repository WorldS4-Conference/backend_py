
# Create your views here.

from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from api.models import *
from api.views.utils import *
from api.models import *


@api_view(['POST'])
def check_tags(request):
    # data = request.data
    # tags = data.get
    tags = request.POST.getlist('tags')
    email = request.POST.getlist('email')
    file_names = request.POST.getlist('filenames')

    existing_file = File.objects.filter(tag__in=tags)
    accessId = None
    tmp = existing_file.exists()
    print(existing_file.exists())
    print(type(existing_file.exists()))

    # if existing_file.exists() == False:
    # print(email)

    print("Tags : ")
    print(tags)

    mht = hashOfHash(tags)
    print("MHT  : ", mht)

    hash_obj = hashlib.sha256(str(email[0]+mht).encode())
    accessId = hash_obj.hexdigest()

    for tag, file_name in zip(tags, file_names):
        File.objects.create(location=file_name, accessId=accessId, tag=tag)

    return JsonResponse({'exists': tmp, 'accessId': accessId})
