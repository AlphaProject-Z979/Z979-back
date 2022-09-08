from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response

from .serializers import ChallengeSerializer
from .models import Challenge, UserChallenge
from .dto.find_challenge_dto import FindChallengeTypeDto
from .dto.find_challenge_type_feed_dto import FindChallengeFeedDto
from feeds.models import Feed
from profiles.models import User
from .serializers import UserChallengeSerializer
from dateutil.relativedelta import relativedelta
import datetime

import json

# 챌린지 등록
# TODO: 챌린지 중복 등록 방지기능
@api_view(['POST'])
def register_challenge(request):

    serialize = ChallengeSerializer(data=request.data)

    if serialize.is_valid():
        serialize.save()

        return HttpResponse(status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# 챌린지 종류 조회
@api_view(['GET'])
def find_challenge_list(request):
    challenges = Challenge.objects.all()

    data = []
    for challenge in challenges:
        # print(challenge.)
        res_dict = FindChallengeTypeDto(
            challenge.challenge_name,
            challenge.challenge_description,
            challenge.image.url
        ).__dict__
        data.append(res_dict)

    return Response({"data" : data},status=status.HTTP_200_OK)

# 1. 챌린지 조회
# 2. 피드에서 해당 챌린지 조회
# 3. response
@api_view(['GET'])
def challenge_detail_feed(request, challenge_id):
    challenge_data = []

    challenge_info = Challenge.objects.get(id = challenge_id)
    challenge_data.append({"challenge_name" : challenge_info.challenge_name,
                           "challenge_description" : challenge_info.challenge_description})

    feed_data = []
    feeds = Feed.objects.filter(challenge_id = challenge_id)
    for feed in feeds:
        res_feed_dict = FindChallengeFeedDto(
            feed.content,
            feed.hashtags,
            feed.image.url
        ).__dict__
        feed_data.append(res_feed_dict)



    return JsonResponse({
        "feed_data" : feed_data,
        "challenge_data" : challenge_data
    },status=200, safe=False)

# 챌린지 참여하기
@api_view(['POST'])
def participate_challenge(request,challenge_id, user_id):
    challenge = Challenge.objects.filter(id=challenge_id)

    if not challenge:
        return Response({"message" : "존재하지 않는 챌린지 입니다."}, status.HTTP_400_BAD_REQUEST)

    user = User.objects.filter(id=user_id)

    if not user:
        return Response({"message": "존재하지 않는 유저 입니다."}, status.HTTP_400_BAD_REQUEST)

    today = datetime.date.today()
    end_date = today + relativedelta(months=1)


    user_challenge = UserChallenge()
    user_challenge.user = user[0]
    user_challenge.challenge = challenge[0]
    user_challenge.end_date = end_date
    user_challenge.save()

    challenge[0].count += 1
    challenge[0].save()


    return Response({"start": today, "end":user_challenge.end_date}, status.HTTP_200_OK)

