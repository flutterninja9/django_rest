from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from .models import Counter
from .serializers import CounterSerializer


def index(request):
    return JsonResponse({
        "id": 1,
        "count": 0,
    })


class CounterViewSet(ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
