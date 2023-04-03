
# Create your views here.

import os
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse, HttpResponse, JsonResponse, StreamingHttpResponse
from api.models import *


@api_view(['POST'])
def download_file(request):

    tag = request.data.get('tag', None)
    # print(tag)

    try:
        file = File.objects.get(tag=tag)
        print(file.location)
        file_name = file.location

        file_path = 'storage/'+file_name  # Replace with your file path
        file = open(file_path, 'rb')

        # Create the streaming response
        response = StreamingHttpResponse(iter(lambda: file.read(65536), b''), content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
        
        # Return the response
        return response

        # if os.path.exists(file_path):
        #     with open(file_path, 'rb') as file:
        #         response = FileResponse(file)
        #         response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)

        #     return response
        # else:
        #     return JsonResponse({'message': "File not found in the server"}, status=404)

        # return HttpResponse("Hello, world!")

        # Do something with the file location
    except File.DoesNotExist:
        return JsonResponse({'message': "File not found"}, status=404)

