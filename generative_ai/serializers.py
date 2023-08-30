from rest_framework import serializers
from .models import BusinessAI, About, ScrollCard


class BusinessAISerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessAI
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class ScrollCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrollCard
        fields = '__all__'
