from django.db import models
from profiles.models import User

# 챌린지 이름
# 챌린지 설명
# 참여 인원
def upload_to(instance, filename):
    import os
    from random import randint
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)

    return 'feeds/%s' % (
        # instance.id,
            now().strftime('%Y%m%d') + '_' + str(randint(10000000, 99999999))
    )

class Challenge(models.Model):
    challenge_name = models.CharField(max_length=100, null=False)
    challenge_description = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to=upload_to, null=True)
    count = models.IntegerField(default=0)




# 유저(foreign key)
# 챌린지(foreign key)
# 시작 날짜
# 종료 날짜
class UserChallenge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now = True)
    end_date = models.DateField()
    progress = models.BooleanField(default=True)

    def create(cls, user, challenge, end_date):
        user_challenge = cls(user,challenge,end_date)

        return user_challenge