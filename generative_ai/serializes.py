from rest_framework import serializers
from .models import BusinessAI

class importBusinessAISerializer(serializers.ModelSerializer):
  class Meta:
    model=BusinessAI
    fields= '__all__'
    