from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Feed
from .serializers import FeedSerializer
from challenge.models import Challenge
from challenge.serializers import ChallengeSerializer
import json

class PostFeedTest(APITestCase):
    def setUp(self):
        serialize = ChallengeSerializer(data={
            "challenge_name": "CN",
            "challenge_description": "CD"
        })

        if serialize.is_valid():
            serialize.save()

    def test_post_feed(self):
        challenge = Challenge.objects.get(id=1)

        url = reverse("post_feed",kwargs={"user_id":1})

        post_feed_data = {
            "content": "post feed test content",
            "hashtags": "post feed hashtags",
            "challenge" : challenge.id
        }

        response = self.client.post(url, json.dumps(post_feed_data),content_type="application/json")


        self.assertEqual(response.status_code, 201)


class FeedTest(APITestCase):
    def setUp(self):
        serialize = ChallengeSerializer(data={
            "challenge_name": "CN1",
            "challenge_description": "CD1"
        })

        if serialize.is_valid():
            serialize.save()

        serialize = ChallengeSerializer(data={
            "challenge_name": "CN2",
            "challenge_description": "CD2"
        })

        if serialize.is_valid():
            serialize.save()

        self.data = {
            "content": "OC",
            "hashtags": "OH 주워요",
            "challenge": 1,
            "is_challenge" : True
        }

        for i in range(2):
            feed_serialize = FeedSerializer(data=self.data)

            if feed_serialize.is_valid():
                challenge = Challenge.objects.get(id=1)
                feed_serialize.validated_data['challenge'] = challenge
                feed_serialize.save()

        for i in range(2):
            feed_serialize = FeedSerializer(data=self.data)

            if feed_serialize.is_valid():
                challenge = Challenge.objects.get(id=2)
                feed_serialize.validated_data['challenge'] = challenge
                feed_serialize.save()

        feed_serialize = FeedSerializer(data=self.data)

        if feed_serialize.is_valid():
            challenge = Challenge.objects.get(id=1)
            feed_serialize.validated_data['challenge'] = None
            feed_serialize.validated_data['is_challenge'] = False
            feed_serialize.save()

    def test_update_feed(self):
        url = reverse("update_feed",kwargs={"user_id":1,"feed_id":1})
        update_feed_data = {
            "content": "UC",
            "hashtags": "UH",
            "challenge" : 1
        }

        response = self.client.put(url, update_feed_data)
        res_data = json.loads(response.data['data'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_data['content'],'UC')



    def test_like_feed(self):
        url = reverse("like_feed", kwargs={"feed_id" : 2})

        response = self.client.put(url)

        self.assertEqual(response.data['like'], 1)

class FindTest(APITestCase):
    def setUp(self):

        serialize = ChallengeSerializer(data={
            "challenge_name": "CN1",
            "challenge_description": "CD1"
        })

        if serialize.is_valid():
            serialize.save()

        serialize = ChallengeSerializer(data={
            "challenge_name": "CN2",
            "challenge_description": "CD2"
        })

        if serialize.is_valid():
            serialize.save()

        self.data = {
            "content": "OC",
            "hashtags": "OH 주워요",
            "challenge": 1,
            "is_challenge" : True
        }

        for i in range(4):
            feed_serialize = FeedSerializer(data=self.data)

            if feed_serialize.is_valid():
                challenge = Challenge.objects.get(id=1)
                feed_serialize.validated_data['challenge'] = challenge
                feed_serialize.validated_data['like'] = i+1
                feed_serialize.save()

        feed_serialize = FeedSerializer(data=self.data)

        if feed_serialize.is_valid():
            challenge = Challenge.objects.get(id=1)
            feed_serialize.validated_data['challenge'] = challenge
            feed_serialize.save()

        for i in range(2):
            feed_serialize = FeedSerializer(data=self.data)

            if feed_serialize.is_valid():
                challenge = Challenge.objects.get(id=2)
                feed_serialize.validated_data['challenge'] = challenge
                feed_serialize.validated_data['like'] = i + 1
                feed_serialize.save()

        feed_serialize = FeedSerializer(data=self.data)

        if feed_serialize.is_valid():
            challenge = Challenge.objects.get(id=1)
            feed_serialize.validated_data['challenge'] = None
            feed_serialize.validated_data['is_challenge'] = False
            feed_serialize.save()

    def test_find_all_feed(self):
        url = reverse("find_all_feed")

        response = self.client.get(url)
        self.assertEqual(response.data['feed_cnt'], 5)

    def test_find_challenge_feed(self):
        url = reverse("find_challenge_feed", kwargs={"challenge_id" : 1})

        response = self.client.get(url)

        self.assertEqual(response.data['data'][0]['like'], 4)
        self.assertEqual(response.data['data'][-1]['like'], 0)
        self.assertEqual(len(response.data['data']), 5)



