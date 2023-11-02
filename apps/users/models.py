from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from apps.users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'password']

    class Meta:
        app_label = 'users'
        verbose_name = 'User'


class Questionnaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=400)
    activity = models.CharField(max_length=100)
    work_experience = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    social = models.CharField(max_length=100)
    schedule = models.TimeField()
    schedule_end = models.TimeField()
    area = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user} - {self.name}'

    class Meta:
        verbose_name = 'Анкеты'
        verbose_name_plural = 'Анкета'
