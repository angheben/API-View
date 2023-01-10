from django.urls import path, include
from .views import HelloApiView

urlpatterns = [
    path('hello_world/', HelloApiView.as_view()),
]