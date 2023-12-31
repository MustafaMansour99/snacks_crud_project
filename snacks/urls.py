from django.contrib import admin
from django.urls import path
from .views import SnackListView,SnackDetailsListView,SnackCreateView,SnackUpdateView,SnackDeleteView   
urlpatterns = [
path('',SnackListView.as_view(), name="snacks"),
path('<int:pk>/',SnackDetailsListView.as_view(), name="snack_detail"),
path('create/',SnackCreateView.as_view(), name="snack_create"),
path('<int:pk>/update/',SnackUpdateView.as_view(), name="snack_update"),
path('<int:pk>/delete/',SnackDeleteView.as_view(), name="snack_delete"),
]