from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    restaurant_name = serializers.CharField()
    menu_name = serializers.CharField()
    category = serializers.CharField()
    price = serializers.FloatField()
    spicy_level = serializers.IntegerField()
    is_available = serializers.BooleanField()
    description = serializers.CharField(allow_blank=True)
    created_at = serializers.DateTimeField(read_only=True)