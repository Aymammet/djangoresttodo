import django
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Task
from . serializer import TaskSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['title']
    ordering_fields = ['title', 'status', 'priority']
    ordering = ['-created_date']
    pagination_class = PageNumberPagination
    filter_fields = ['status']

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

