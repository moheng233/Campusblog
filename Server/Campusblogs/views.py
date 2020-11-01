from collections import OrderedDict
from rest_framework.response import Response
from Campusblogs.models import Blogs
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from Campusblogs.serializers import BlogsListSerializer, BlogsSerializer

from rest_framework.pagination import PageNumberPagination

class BlogPagePagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('results', data)
        ]))

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = BlogsListSerializer

    pagination_class = BlogPagePagination

    def get_serializer_class(self):
        if(self.action == 'list'):
            return BlogsListSerializer
        elif self.action == 'update':
            return BlogsSerializer
        elif self.action == 'retrieve':
            return BlogsSerializer
        elif self.action == 'create':
            return BlogsSerializer
        else:
            return super().get_serializer_class()