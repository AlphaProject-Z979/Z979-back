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

def upload_to(instance, filename):
    import os
    from random import randint
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)

    return 'feeds/%s' % (
        # instance.id,
            now().strftime('%Y%m%d') + '_' + str(randint(10000000, 99999999))
    )

class Feed(models.Model):
    content = models.CharField(max_length=100)
    hashtags = models.CharField(max_length=100)
    like = models.IntegerField(default=0)
    challenge = models.ForeignKey(Challenge,on_delete=models.CASCADE, null=True)
    is_challenge = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to, null=True)
    is_get_stamp = models.BooleanField(default=False)



    def set_hashtag(self, tags):
        self.hashtag = json.dumps(tags)

    def get_hashtag(self):
        return json.loads(self.hashtag)


    def like_feed(self):
        self.like += 1
        return self.like


class FeedImage(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
