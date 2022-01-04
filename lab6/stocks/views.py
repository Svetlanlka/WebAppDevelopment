from rest_framework import viewsets
from stocks.serializers import DonutSerializer, DonutsSetSerializer
from stocks.models import Donut, DonutsSet

class DonutViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать пончики
    """
    # queryset всех пончиков для фильтрации по стоимости пончика
    queryset = Donut.objects.all().order_by('cost')
    serializer_class = DonutSerializer  # Сериализатор для модели

class DonutsSetViewSet(viewsets.ModelViewSet):
    queryset = DonutsSet.objects.all()
    serializer_class = DonutsSetSerializer