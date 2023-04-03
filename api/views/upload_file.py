
# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from api.models import *

@api_view(['POST'])
def upload_file(request):

    # serializer = UploadedFileSerializer(data=request.data)
    # if serializer.is_valid():
    # Get the uploaded file
    # uploaded_file = request.FILES['file']

    tag = request.data.get('tag', None)
    print(tag)

    for file_name, uploaded_file in request.FILES.items():
        file_content = uploaded_file.read()
        print(uploaded_file)

        with open('storage/' + uploaded_file.name, 'wb') as f:
            f.write(file_content)
            UploadedFile.objects.create(tag=tag, location=uploaded_file.name)

    return HttpResponse("Hello, world!")

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
