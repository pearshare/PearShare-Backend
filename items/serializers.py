from rest_framework import serializers
from items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    def get_user(self, obj):
      return obj.user.username
      
    class Meta:
        model = Item
        fields = ('id', 'title', 'image_b64_addr', 'description', 'seller', \
        'price', 'status', 'best_before_date', 'created', 'modified')

