from rest_framework import serializers

from api.serializers import UserSerializer
from post import models


class PostViewSetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Post
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        return models.Post.objects.create(**validated_data, user=user)
