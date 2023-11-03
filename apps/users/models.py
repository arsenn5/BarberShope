from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from apps.users.constants import LANGUAGE, WORK_EXPERIENCE, AREA
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


class Service(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

#{
#     "title": "eldiloh",
#     "price": 123
# }
class Questionnaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Имя', null=True)
    image = models.ImageField(null=True, verbose_name='Фото')
    date = models.DateField(auto_now_add=True, null=True, verbose_name='Последняя изминение')
    description = models.TextField(max_length=400, null=True, verbose_name='O себе')
    activity = models.CharField(max_length=100, null=True, verbose_name='Деятельность')
    work_experience = models.CharField(choices=WORK_EXPERIENCE, max_length=100, null=True, verbose_name='Стаж работы')
    language = models.CharField(choices=LANGUAGE, max_length=100, null=True, verbose_name='Язык')
    phone_number = PhoneNumberField(null=True, verbose_name='Телефон номер')
    social = models.URLField(max_length=100, null=True, verbose_name='Соц сети')
    schedule = models.TimeField(null=True, verbose_name='Начало график работы')
    schedule_end = models.TimeField(null=True, verbose_name='Конец график работы')
    area = models.CharField(choices=AREA, null=True, max_length=100, verbose_name='Район')
    service = models.ManyToManyField(Service)

    def __str__(self):
        return f'{self.user} - {self.name}'

    class Meta:
        verbose_name = 'Анкеты'
        verbose_name_plural = 'Анкета'
