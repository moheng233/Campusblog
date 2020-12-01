from collections import OrderedDict

from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from Campusblogs.models import Blogs, Classify, Posts, Reports, UploadImages
from Campusblogs.serializers import (BlogsListSerializer, BlogsSerializer, ClassifyListSerializer, ClassifySerializer,
                                     PostSerializer, ReportsSerializer, UploadImagesSerializer)


class BlogPagePagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('results', data)
        ]))

# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.filter(activation=True).all()
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

    def get_permissions(self):
        if(self.action == "list"):
            return []
        else:
            return super().get_permissions()
        pass


class ClassifyViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
        queryset = Classify.objects.all()
        serializer_class = ClassifyListSerializer

        
        def get_serializer_class(self):
            if(self.action == "list"):
                return ClassifyListSerializer
            elif (self.action == "retrieve"):
                return ClassifySerializer
            else:
                return super().get_serializer_class()
        pass

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class ReportsViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer


class UploadImagesViewSet(viewsets.ModelViewSet):
    queryset = UploadImages.objects.all()
    serializer_class = UploadImagesSerializer
