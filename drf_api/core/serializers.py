from rest_framework import serializers
from .models import Core


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'created_at')
        model = Core
