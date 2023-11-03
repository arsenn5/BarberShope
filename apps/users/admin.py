from django.contrib import admin
from .models import User, Questionnaire, Service, Review

# Register your models here.
admin.site.register(User)
admin.site.register(Questionnaire)
admin.site.register(Service)
admin.site.register(Review)
