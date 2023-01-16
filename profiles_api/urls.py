from django.urls import path, include
from .views import HelloApiView, HelloViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello_viewset', HelloViewSet, basename='hello_viewset')

urlpatterns = [
    path('hello_world/', HelloApiView.as_view()),
    path("", include(router.urls))
]