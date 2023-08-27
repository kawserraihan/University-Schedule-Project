from django.shortcuts import render
from info.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.authtoken.models import Token
#from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
#from itertools import chain
from rest_framework import serializers, status
from rest_framework.generics import ListAPIView
from django.db.models.signals import post_save
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from django.db.models import Sum, Count
from django.conf import settings
import apis.serializers as api_ser
from django.http import JsonResponse
from django.http import HttpResponseRedirect

from apis.serializers import BatchSerializer, SectionSerializer, ClassDetailsSerializer

class BatchListByDept(APIView):
    def get(self, request, dept_id):
        batches = Batch.objects.filter(department_id=dept_id)
        serializer = BatchSerializer(batches, many=True)
        return JsonResponse(serializer.data, safe=False)
    

class SectionByDept(APIView):
    def get(self, request, dept_id, batch_id):
        try:
            section = Section.objects.filter(department_id = dept_id, batch_id = batch_id)
            serializer = SectionSerializer(section, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Section.DoesNotExist:
            return Response(status=404)
        
class ClassDetailsAll(APIView):
    def get(self, request, dept_id, batch_id, section_id):
        try:
            
            classdetails= ClassDetails.objects.filter(department_id = dept_id, batch_id = batch_id, section_id = section_id)
            serializer = ClassDetailsSerializer(classdetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except ClassDetails.DoesNotExist:
            return Response(status=404)
