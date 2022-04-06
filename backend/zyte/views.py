from rest_framework import viewsets
from django_filters import rest_framework as filters

from .serializers import JobDataSerializer,  SpiderSerializer
from .models import JobData, Spider
from .mixins import ManyOnListMixin, NoReturnCreateModelMixin

class SpiderViewSet(ManyOnListMixin, viewsets.ModelViewSet):
    queryset = Spider.objects.all()
    serializer_class = SpiderSerializer

class JobDataViewSet(ManyOnListMixin, NoReturnCreateModelMixin, viewsets.ModelViewSet):
    queryset = JobData.objects.all().order_by('date')
    serializer_class = JobDataSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("spider", )