from django.shortcuts import render
from .models import DemandePret
from rest_framework import viewsets
from rest_framework.serializers import ModelSerializer


class DemandeSerializer(ModelSerializer):
     class Meta:
        model = DemandePret
        fields = ['name']


class DemandeViewSet(viewsets.ModelViewSet):
    queryset = DemandePret.objects.all()
    serializer_class = DemandeSerializer