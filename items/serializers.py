from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'image_b64_addr', 'description', 'seller', \
        'price', 'sold', 'best_before_date', 'created', 'modified')
