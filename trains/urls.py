
from django.urls import path

from trains.views import *

urlpatterns = [
    path('', TrainListView.as_view(), name='trains'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='trains_detail'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='trains_update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='trains_delete'),
    path('add/', TrainCreateView.as_view(), name='trains_create'),

]
