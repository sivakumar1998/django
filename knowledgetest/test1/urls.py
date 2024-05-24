from django.urls import path
from . import views

urlpatterns = [
    path("greet/<str:id>",views.greet)
]
