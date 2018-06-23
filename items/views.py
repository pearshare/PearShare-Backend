from items.models import Item
from items.serializers import ItemSerializer
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def update_status(request, item_id):
    item = Item.objects.get(id=item_id)
    item.status = "transacted"
    item.save()
    return JsonResponse({"message": "success"})