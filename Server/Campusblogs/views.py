from collections import OrderedDict

from constance import config
from django.contrib.auth.models import User
from django.db.models import F
from django.db.models.manager import BaseManager
from django.shortcuts import render
from rest_framework import filters, mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from Campusblogs.models import Blogs, Classify, Posts, Reports, UploadImages
from Campusblogs.serializers import (
    BlogsListSerializer,
    BlogsSerializer,
    AddFabulousSerializer,
    ClassifyListSerializer,
    ClassifySerializer,
    PostSerializer,
    ReportsSerializer,
    UploadImagesSerializer,
)


class BlogPagePagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(
            OrderedDict([("count", self.page.paginator.count), ("results", data)])
        )


# Create your views here.


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.filter(activation=True,user__is_active=True).all()
    serializer_class = BlogsListSerializer

    pagination_class = BlogPagePagination

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)

    search_fields = ("title","=user__username")
    ordering_fields = ("fabulous","created_at", "updated_at")
    classify_fields = "classify"

    def get_queryset(self):
        queryset: BaseManager = super().get_queryset()

        classify_params = self.request.query_params.get("classify", None)
        if classify_params is not None:
            classify = Classify.objects.get(id=classify_params)
            queryset = queryset.filter(classify=classify)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return BlogsListSerializer
        elif self.action == "update":
            return BlogsSerializer
        elif self.action == "retrieve":
            return BlogsSerializer
        elif self.action == "create":
            return BlogsSerializer
        else:
            return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "list":
            return []
        else:
            return super().get_permissions()
        pass

    def sensitive_testing(self, serializer):
        Sensitive: str = getattr(config, "sensitive_words")
        SensitiveList = Sensitive.split(",")
        for s in iter(SensitiveList):
            if s in serializer.initial_data["title"]:
                raise APIException(detail="标题包含敏感词'" + s + "'")
            pass
            if s in serializer.initial_data["content"]:
                raise APIException(detail="正文包含敏感词'" + s + "'")
            pass

    @action(["GET"], detail=True, url_name="Add Fabulous", url_path="add_fabulous")
    def add_fabulous(self, request: Request, *args, **kwargs):
        blog = self.get_object()
        blog.fabulous = F('fabulous') + 1
        blog.save()

        return Response(status=status.HTTP_204_NO_CONTENT,data={})

    def perform_create(self, serializer):
        self.sensitive_testing(serializer)
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        self.sensitive_testing(serializer)
        return super().perform_update(serializer)


class ClassifyViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Classify.objects.all()
    serializer_class = ClassifyListSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ClassifyListSerializer
        elif self.action == "retrieve":
            return ClassifySerializer
        else:
            return super().get_serializer_class()

    pass

    def get_permissions(self):
        if self.action == "list":
            return []
        else:
            return super().get_permissions()
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

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == "list":
            queryset = queryset.filter(user=self.request.user)

        return queryset
