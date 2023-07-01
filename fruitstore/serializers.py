from rest_framework import serializers

from fruitstore.models import FruitStore, FruitMenu


class FruitMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitMenu
        fields = '__all__'


class FruitStoreSerializer(serializers.ModelSerializer):
    fruitMenus = FruitMenuSerializer(many=True, read_only=True)

    class Meta:
        model = FruitStore
        fields = '__all__'
