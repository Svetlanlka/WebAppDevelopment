from stocks.models import Donut, DonutsSet
from rest_framework import serializers

class DonutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donut
        fields = ["pk", "name", "info", "cost"]

class DonutsSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonutsSet
        fields = ["pk", "name", "info"]