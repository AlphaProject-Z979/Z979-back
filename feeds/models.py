import json

from django.db import models
from challenge.models import Challenge
from profiles.models import User
# 본문
# 해시태그
# 이미지
# 좋아요
# 챌린지 여부
# 유저
class Feed(models.Model):
    content = models.CharField(max_length=100)
    hashtags = models.CharField(max_length=100)
    like = models.IntegerField(default=0)
    challenge = models.ForeignKey(Challenge,on_delete=models.CASCADE, null=True)
    is_challenge = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def set_hashtag(self, tags):
        self.hashtag = json.dumps(tags)

    def get_hashtag(self):
        return json.loads(self.hashtag)

class FeedImage(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
