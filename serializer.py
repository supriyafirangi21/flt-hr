
from rest_framework import serializers
from .models import Activity_user, Activity_periods

class Activity_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity_user
        fields = '__all__'

class Activity_periodsSerializer(serializers.ModelSerializer):
    #Activity_user = Activity_userSerializer(many=True)
    class Meta:
        model = Activity_periods
        fields = ('start_time','end_time')
