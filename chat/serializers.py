from rest_framework import serializers

from chats import models

class UserSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(default=0)

    class Meta:
        model = models.Profile
        fields = ("id", "user", "avatar", "count")


class MessageCreateSerializer(serializers.ModelSerializer):
    contact = ProfileSerializers(read_only=True)

    class Meta:
        model = models.Message
        fields = ("contact", "message", "voice", "location", "is_watched", "images", "documents")



class ChatSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(default=0)
    sender = serializers.StringRelatedField()

    message = MessageCreateSerializer()

    class Meta:
        model = models.Chat
        fields = ("id", "sender", "recipient", "message", "is_watched", "count", "created_ad")