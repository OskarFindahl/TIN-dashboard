from rest_framework import viewsets
from .serializers import JobDataSerializer,  SpiderSerializer
from .models import JobData, Spider
from .mixins import ManyOnListMixin, NoReturnCreateModelMixin

class SpiderViewSet(ManyOnListMixin, viewsets.ModelViewSet):
    queryset = Spider.objects.all()
    serializer_class = SpiderSerializer

class JobDataViewSet(ManyOnListMixin, NoReturnCreateModelMixin, viewsets.ModelViewSet):
    queryset = JobData.objects.all()
    serializer_class = JobDataSerializer