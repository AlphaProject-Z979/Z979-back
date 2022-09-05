from allauth.account.adapter import DefaultAccountAdapter
from .models import User

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email
        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image
        nickname = data.get("nickname")
        profile_image = data.get("profile_image")
        user.profile_image = profile_image
        print(data)

        if nickname :
            user.nickname = nickname

        user.save()
        
        return user