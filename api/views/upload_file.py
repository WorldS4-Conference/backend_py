
# Create your views here.

import json
import os
import traceback
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from api.models import *
from api.views.utils import *


from charm.toolbox.pairinggroup import PairingGroup, GT
from CP_ABE_for_files.utils import *
from CP_ABE_for_files.CPabe09 import *
from CP_ABE_for_files.constants import *


def encrypt_and_store_file_key(groupObj, file_path, cpabe, master_public_key, policy):
    # Using random element from the GT group to encrypt the file using AES
    print("file_path = ", file_path)
    message = groupObj.random(GT)
    key_str = grp_to_str(message)
    encrypt_file(file_path, key_str)
    file_name = os.path.basename(file_path)

    # print("AES Key = ", message)

    # Encrypting the key and storing it in file
    encrypted_key_message = cpabe.encrypt(master_public_key, message, policy)
    # print("encrypted_key_message = ", encrypted_key_message)
    encrypted_key_message_serialised = encrypted_key_message.copy()
    serialize_dict_elements(encrypted_key_message_serialised, groupObj)
    # print(encrypted_key_message_serialised)
    with open('keys/'+file_name+'.json', 'w') as f:
        json.dump(encrypted_key_message_serialised, f)


@api_view(['POST'])
def upload_file(request):
    print("upload file")

    # Initializing CPABE System
    # Get the elliptic curve with the bilinear mapping feature needed.
    groupObj = PairingGroup('SS512')
    cpabe = CPabe09(groupObj)
    (master_private_key, master_public_key) = cpabe.setup(g1=g1, g2=g2, alpha=alpha, a=a)

    try:
        tag = request.data.get('tag', None)
        accessId = request.data.get('accessId', None)
        policy = request.data.get('policy', None)
        print(tag)
        print(policy)

        for file_name, uploaded_file in request.FILES.items():
            file_content = uploaded_file.read()
            print(uploaded_file)

            with open('storage/' + uploaded_file.name, 'wb') as f:
                f.write(file_content)

            tag = hashFile('storage/' + uploaded_file.name)

            encrypt_and_store_file_key(
                groupObj, 'storage/' + uploaded_file.name, cpabe, master_public_key, policy)

            print("done till here")

            print(accessId, tag.hex())

            # File.objects.update()

            # file =
            File.objects.filter(accessId=accessId, tag=tag.hex()).update(
                location=uploaded_file.name)
            # print(file)
            # file = files[0]
            # file.location = uploaded_file.name
            # print(file)
            # file.save()

        return JsonResponse({"message": "File Uploaded Succesfully"}, status=200)
    except Exception as e:
        traceback.print_exc()  # Print the full traceback to the console
        return JsonResponse({"message": str(e)}, status=500)
