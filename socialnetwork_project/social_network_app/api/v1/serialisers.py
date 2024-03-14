from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from social_network_app.models import Publications, Comments, Reposts
from generic_relations.relations import GenericRelatedField


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


class RepostSerializer(ModelSerializer):
    class Meta:
        model = Reposts
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
