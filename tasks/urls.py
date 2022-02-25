from django.urls import  path, include
from .views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("", TaskViewSet, basename='todo')

urlpatterns = [
    path('', include(router.urls)),
]

