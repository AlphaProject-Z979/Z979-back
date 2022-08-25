class AllFeedDto:
    def __init__(self):
        self.data = []

# 본문
# 유저 이름
# 해시태그
# 이미
class SpecificFeedDto:
    def __init__(self, nickname, content, hashtags,like, is_challenge):
        self.nickname = nickname
        self.content = content
        self.hashtags = hashtags
        self.like = like
        self.is_challenge = is_challenge