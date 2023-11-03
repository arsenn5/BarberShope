from django.contrib import admin
from apps.users.models import User, Questionnaire, Service

# Register your models here.
admin.site.register(User)
admin.site.register(Questionnaire)
admin.site.register(Service)
