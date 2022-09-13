from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from profiles.models import User
from .serializers import StampSerializer
from .models import Stamp

# 스탬프 조회
@api_view(['GET'])
def find_my_stamps(request, user_id):
    stamps = Stamp.objects.filter(user=user_id)

    challenges_stamps = 0
    campaign_stamps = 0

    for stamp in stamps:
        if stamp.is_challenge:
            challenges_stamps += 1
        else:
            campaign_stamps += 1

    return Response({"challenge_stamps" : challenges_stamps,
                     "campaign_stamps" : campaign_stamps},status=status.HTTP_200_OK)



# Create your views here.
