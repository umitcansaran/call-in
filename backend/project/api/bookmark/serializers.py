from rest_framework import serializers
from .models import BookmarkModel


class BookmarkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookmarkModel
        fields = ['event', 'call', 'organisation', 'volunteer', 'id']
        read_only_fields = fields
