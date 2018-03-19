from .models import *
from django.http import Http404
from django.shortcuts import get_object_or_404

from .serializer import *

from rest_framework.views import APIView
from rest_framework.response import Response


class CniDetail(APIView):
    """
        Retrieve, update or delete a cni instance
    """
    def get_object(self, cniNber):
        try:
            return Cni.objects.get(nberCni=cniNber)
        except Cni.DoesNotExist:
            raise Http404
    
    def get(self, request, cniNber, format=None):
        cni = self.get_object(cniNber)
        cni = CniSerializer(cni)
        return Response(cni.data)


class RecepDetail(APIView):
    """
        Retrieve, update or delete a recept instance
    """
    def get_object(self, recepNber):
        try:
            return Recep.objects.get(nberRecep=recepNber)
        except Recep.DoesNotExist:
            raise Http404
    
    def get(self, request, recepNber, format=None):
        recep = self.get_object(recepNber)
        recep = RecepSerializer(recep)
        return Response(recep.data)


class CniAdvancedDetail(APIView):
    """
        Retrieve, update or delete an product instance
    """
    def get_object(self, name, surname, birthdate):
        try:
            return Cni.objects.get(name=name, surname=surname, birthdate=birthdate)
        except Cni.DoesNotExist:
            raise Http404

    def get(self, request, name, surname, birthdate, format=None):
        cni = self.get_object(name, surname, birthdate)
        cni = CniSerializer(cni)
        return Response(cni.data)