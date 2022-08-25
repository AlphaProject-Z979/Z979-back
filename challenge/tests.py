from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Challenge
from .serializers import ChallengeSerializer


# Create your tests here.
class RegistChallengeTest(APITestCase):
    def test_register_challenge(self):

        url = reverse("register_challenge")
        challenge_data = {
            "challenge_name": "줍깅",
            "challenge_description": "쓰레기를 주워요"
        }

        response = self.client.post(url, challenge_data)

        self.assertEqual(response.status_code, 201)

    # 챌린지 설명 없이 챌린지 등록 시 400에러
    def test_fail_without_description(self):
        url = reverse("register_challenge")
        challenge_data = {
            "challenge_name": "줍깅"
        }

        response = self.client.post(url, challenge_data)

        self.assertEqual(response.status_code, 400)

    # 챌린지 이름 없이 챌린지 등록 시 400에러
    def test_fail_without_name(self):
        url = reverse("register_challenge")
        challenge_data = {
            "challenge_description": "쓰레기를 주워요"
        }

        response = self.client.post(url, challenge_data)

        self.assertEqual(response.status_code, 400)

class FindChallenges(APITestCase):
    def setUp(self):

        self.data = [
            {
                "challenge_name": "줍깅",
                "challenge_description": "쓰레기를 주워요"
            },
            {
                "challenge_name": "걷기",
                "challenge_description": "걸어봐요"
            }
        ]

        for d in self.data:
            serialize = ChallengeSerializer(data=d)
            if serialize.is_valid():
                serialize.save()


    def test_find_challenge_type(self):
        response = self.client.get(reverse("find_challenges"))

        self.assertEqual(len(response.data['data']),2)
        self.assertEqual(response.status_code, 200)




