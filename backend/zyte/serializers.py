from rest_framework import serializers 
from .models import JobData, Spider

class SpiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spider
        fields = "__all__"


class JobDataSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except:
            pass
        
    class Meta:
        model = JobData
        fields = "__all__"
