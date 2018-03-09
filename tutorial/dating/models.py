import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Area(models.Model):
    province = models.CharField(
        _('省'),
        max_length=10,
        unique=False,
        help_text=_('必须，仅允许不超过10个字母数字。'),
    )
    city = models.CharField(
        _('市'),
        max_length=10,
        unique=False,
        help_text=_('必须，仅允许不超过10个字母数字。'),
    )
    region = models.CharField(
        _('区'),
        max_length=10,
        unique=False,
        help_text=_('必须，仅允许不超过10个字母数字。'),
    )

    def __str__(self):
        return 'place: {} {} {}'.format(self.province, self.city, self.region)


# class UserText(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
#     email = models.CharField(_('邮箱'), max_length=50)
#     phonenum = models.IntegerField(_('手机号'), max_length=11)
#     password = models.CharField(_('密码'), max_length=20)
#     date_of_birth = models.DateTimeField()

# class Membermanager(BaseUserManager):
#     def create_user(self, phone, date_of_birth, password=None):
#         """
#         Creates and saves a User with the given phone number,  date of
#         birth and password.
#         """
#         if not phone:
#             raise ValueError('Users must have an phone number')
#
#         user = self.model(
#             phone=self.normalize_phone(phone),
#             date_of_birth=date_of_birth,
#         )
#         user.is_superuser = False
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#
#     def create_superuser(self, phone, date_of_birth, password):
#         """
#         Creates and saves a superuser with the given phone, date of
#         birth and password.
#         """
#         user = self.create_user(phone,
#                                 password=password,
#                                 date_of_birth=date_of_birth
#                                 )
#         user.is_admin = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    phone = models.CharField(
        verbose_name='phone number',
        max_length=11,
        unique=True,)
    gender = models.CharField(_('性别'), max_length=2)
    username = models.CharField(_('昵称'), max_length=24)
    age = models.IntegerField(_('年龄'), default=0)
    name = models.CharField(_('真实姓名'), max_length=10)
    height = models.CharField(_('身高（厘米）'), max_length=6)
    income = models.CharField(_('年薪（人民币）'), max_length=100)
    wechat = models.CharField(_('微信号'), max_length=30)
    introduce = models.CharField(_('自我介绍'), max_length=1024)
    department = models.CharField(_('工作单位'), max_length=1024)
    station = models.CharField(_('工作岗位'), max_length=80)
    hometown = models.ForeignKey(Area, on_delete=models.SET_DEFAULT, default=None, related_name='hometown_list')
    residence = models.ForeignKey(Area, on_delete=models.SET_DEFAULT, default=None, related_name='residence_list')

    #
    # def get_full_name(self):
    #     # The user is identified by their email address
    #     return self.phone
    #
    # def get_short_name(self):
    #     # The user is identified by their email address
    #     return self.phone

    def __str__(self):
        return self.phone


class Attention(models.Model):
    id = models.AutoField(_('关注编号'), primary_key=True)
    befollowed = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=None, related_name='followed_list')
    follower = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=None, related_name='follower_list')
    attentionTime = models.DateTimeField(blank=True, null=True)


class Invitation(models.Model):
    id = models.AutoField(_('邀请编号'), primary_key=True)
    inviter = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=None, related_name='inviter_list')
    invetee = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=None, related_name='invitee_list')
    invitationTime = models.DateTimeField(blank=True, null=True)
    invitationNum = models.ForeignKey(Member, on_delete=models.SET_DEFAULT, default=None, related_name='invitation_list')
