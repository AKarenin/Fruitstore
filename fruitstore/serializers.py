from rest_framework import serializers

from fruitstore.models import FruitStore


class FruitStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitStore
        fields = '__all__'
