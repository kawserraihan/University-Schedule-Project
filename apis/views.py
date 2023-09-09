from django.shortcuts import render
from info.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
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
from apis.serializers import BatchSerializer, SectionSerializer, ClassDetailsSerializer, DeptSerializer
from collections import defaultdict

class BatchListByDept(APIView):
    def get(self, request, dept_id):
        batches = Batch.objects.filter(department__id=dept_id)
        serializer = BatchSerializer(batches, many=True)
        return JsonResponse(serializer.data, safe=False)
    

class SectionByDept(APIView):
    def get(self, request, dept_id, batch_id):
        try:
            section = Section.objects.filter(department__id = dept_id, batch_id = batch_id)
            serializer = SectionSerializer(section, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Section.DoesNotExist:
            return Response(status=404)
        
class ClassDetailsAll(APIView):
    def get(self, request, dept_id, batch_id, section_id):
        try:
            
            classdetails= ClassDetails.objects.filter(department__id = dept_id, batch_id = batch_id, section_id = section_id)
            serializer = ClassDetailsSerializer(classdetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except ClassDetails.DoesNotExist:
            return Response(status=404)
        
class DepartmentAll(APIView):
    def get(self,request):
        dept = Dept.objects.all()
        serializer = DeptSerializer(dept, many=True)
        return JsonResponse(serializer.data, safe=False)
    

class ClassDetailsByDayView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch all ClassDetails data
        queryset = ClassDetails.objects.all()

        # Group the data by 'day'
        grouped_data = defaultdict(list)
        for item in queryset:
            grouped_data[item.day].append({
                "classcode": item.classCode,
                "classsubject": item.classSubject,
                "classroom": item.classRoom,
                "classstart": item.classStart,
                "classend": item.classEnd,
                "teacherinit": item.teacherInit,
            })

        # Convert the grouped data to the desired format
        result = [{"day": day, "class_item": items} for day, items in grouped_data.items()]

        return Response(result)

class BusScheduleByDayView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch all BusSchedule data
        queryset = BusSchedule.objects.all()

        # Group the data by 'day'
        grouped_data = defaultdict(list)
        for item in queryset:
            grouped_data[item.day].append({
                "time_of_day": item.time_of_day,
                "bus_number": item.bus_number,
                "route_name": item.route_name,
            })

        # Convert the grouped data to the desired format
        result = [{"day": day.day, "bus_schedules": items} for day, items in grouped_data.items()]

        return Response(result)