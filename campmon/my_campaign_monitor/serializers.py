from rest_framework import serializers
from .models import subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = subscriber
        fields = ('id', 'email', 'name')