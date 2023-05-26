from django.urls import path
from . import views

urlpatterns = [
    path("process_request/", views.process_request),
]
