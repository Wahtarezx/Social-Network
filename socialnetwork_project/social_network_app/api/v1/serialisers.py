from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from social_network_app.api.v1.models import Publications, Comments


class PublicationsSerializer(ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Publications
        fields = '__all__'

    def get_like_count(self, obj):
        return obj.like_count()


class PublicationsCreateSerializer(ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Publications
        fields = '__all__'

    def get_like_count(self, obj):
        return obj.like_count()
        

class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'
