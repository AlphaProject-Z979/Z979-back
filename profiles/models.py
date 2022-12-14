# from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager

class UserManager(BaseUserManager):

    def create_user(self, email, nickname, username, profile_image ,password=None):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        if not username:
            raise ValueError('must have user name')
        user = self.model(
            email = self.normalize_email(email),
            nickname = self.nickname,
            username = self.username,
            profile_image = self.profile_image
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,password=None):
        user = self.model(
            email = self.normalize_email(email),
            # nickname = nickname,
            # name = name,

        )
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    
    id = models.AutoField(primary_key=True)
    email = models.EmailField(_('email address'), unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    username = models.CharField(default='', max_length=100, null=False, blank=False)
    is_staff = True

    def upload_to(instance, filename):
        return 'pic/%s/%s' % (instance.email, filename)
    
    profile_image = ProcessedImageField(
        blank=True,
        processors=[ResizeToFill(300, 300)],
        upload_to = upload_to,
        format='JPEG',
        options={'quality': 70},
    )

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    point = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        )

    # ???????????? username field??? nickname?????? ??????

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def __str__(self):
        return self.fullname

    def has_perm(self, perm, obj=None):
        return True


    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


    def __str__(self):
        return self.nickname
