from django.db.models import Avg
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User, Questionnaire, Service, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user']


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class QuestionnaireSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True)
    review = ReviewSerializer(many=True, read_only=True, label="Отзывы")
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Questionnaire
        fields = '__all__'
        read_only_fields = ['user']

    def get_average_rating(self, obj):
        average_rating = obj.review.aggregate(Avg('rating'))['rating__avg']
        return average_rating
