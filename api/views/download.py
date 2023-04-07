
# Create your views here.

import json
import os
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import FileResponse, HttpResponse, JsonResponse, StreamingHttpResponse
from CP_ABE_for_files.utils import *
from api.models import *

from charm.toolbox.pairinggroup import PairingGroup, GT
from CP_ABE_for_files.utils import *
from CP_ABE_for_files.CPabe09 import *
from CP_ABE_for_files.constants import *


def decrypt_and_store_file(name, attributes, file_path, encrypted_key_message_deserialized, cpabe, master_public_key,
                           master_private_key):
    print("Name = ", name, " | Attributes = ", attributes)

    user_key = cpabe.keygen(master_public_key, master_private_key, attributes)

    decrypted_message = cpabe.decrypt(
        master_public_key, user_key, encrypted_key_message_deserialized)

    if decrypted_message:
        print("Decryption Successful")
        key_str = grp_to_str(decrypted_message)
        print(key_str)
        decrypt_file(file_path, key_str, 'decrypted_chunks/')
        return 0
        # print("Decrypted message  = ", decrypted_message)
    else:
        print("Decryption Unsuccessful ❌")
        return 1


@api_view(['POST'])
def download_file(request):

    # Initializing CPABE System
    # Get the elliptic curve with the bilinear mapping feature needed.
    groupObj = PairingGroup('SS512')
    cpabe = CPabe09(groupObj)
    (master_private_key, master_public_key) = cpabe.setup(
        g1=g1, g2=g2, alpha=alpha, a=a)

    accessId = request.data.get('accessId', None)
    attributes = request.data.get('attributes', None)
    attributes = attributes.split(', ')

    print('accessId : ', accessId)
    print('attributes : ', attributes)

    # return

    files = File.objects.all().filter(accessId=accessId)

    if len(files) == 0:
        return JsonResponse({"error": "Files not found"}, status=404)
    else:
        print(files)
        # return

        result = 0

        files_data = {}
        for file in files:
            file_name = file.location
            file_path = 'storage/' + file_name

            with open('keys/' + file_name + '.json', 'r') as f:
                encrypted_key = json.load(f)

            deserialize_dict_elements(encrypted_key, groupObj)

            result = decrypt_and_store_file(
                'Soham', attributes, file_path, encrypted_key, cpabe, master_public_key, master_private_key)

            if result == 0:
                with open('decrypted_chunks/'+file_name, 'rb') as f:
                    file_content = f.read()
                    files_data[file_name] = base64.b64encode(
                        file_content).decode('utf-8')  # file_content
            else:
                return JsonResponse({'error': 'Incorrect attributes'}, status=400)
                break

        if result == 0:
            json_data = json.dumps(files_data)

            return JsonResponse(json_data, content_type='application/json', safe=False)
