from django.contrib.auth import get_user_model
from django import forms
from rest_framework import serializers
from myauth.models import Interests


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class InterestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interests
        fields = ('name', )


class UserSerializer(serializers.ModelSerializer):
    interests = serializers.PrimaryKeyRelatedField(queryset=Interests.objects.all(), many=True)
    subscribers_count = serializers.SerializerMethodField()
    subscriptions_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'interests', 'subscribers_count', 'subscriptions_count',
        )

    def subscribers_count(self, obj):
        return obj.subscribers_count()

    def subscriptions_count(self, obj):
        return obj.subscriptions_count()

    def get_subscribers_count(self, obj):
        return obj.subscribers_count()
