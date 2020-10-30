from django.urls import path

from django.contrib import admin
from .views import Activity_periods, UserSerializerView

urlpatterns = [

    path('Activity_periods/',Activity_periods.as_view()),
    path('user_details/', UserSerializerView.as_view()),

]
