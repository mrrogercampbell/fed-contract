from django.urls import path
from . import views

urlpatterns = [
    path('', views.result_list, name='result_list'),
    path('result/<int:pk>', views.result_detail, name='result_detail'),
]
