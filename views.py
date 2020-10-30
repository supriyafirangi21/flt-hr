from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Activity_user,Activity_periods
from .serializer import Activity_userSerializer,Activity_periodsSerializer
from .models import Activity_user, Activity_periods
from .serializer import Activity_periodsSerializer, Activity_userSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter


class Activity_periods(ListAPIView):
    queryset = Activity_periods.objects.all()
    serializer_class = Activity_periodsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['start_time','end_time','id']



class UserSerializerView(ListAPIView):
    queryset = Activity_user.objects.all()
    serializer_class = Activity_userSerializer