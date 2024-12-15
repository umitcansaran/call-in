from rest_framework import serializers

from .models import Focus


class FocusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Focus
        fields = '__all__'
