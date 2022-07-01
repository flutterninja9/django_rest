from django.urls import path

from .views import CounterViewSet, index

urlpatterns = [
    path('', index),
    path('counter', CounterViewSet.as_view({'get': 'list'})),
]
