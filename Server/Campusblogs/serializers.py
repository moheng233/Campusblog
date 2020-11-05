from django.db.models.fields import files
from Campusblog.fields import Base64ImageField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, Serializer

from Campusblogs.models import Blogs, Posts, Reports, UploadImages


class BlogsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'last_name')

class UploadImagesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user = BlogsUserSerializer(read_only = True)
    file = Base64ImageField()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data=validated_data)
        pass

    class Meta:
        model = UploadImages
        fields = ('id','user','file')
        read_only_fields = ('id', 'user')
        
        
class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user = BlogsUserSerializer(read_only = True)


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data=validated_data)
        pass
    class Meta:
        model = Posts
        fields = ('id','user','blog','content','created_at')



class BlogsListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    subimage = UploadImagesSerializer()
    user = BlogsUserSerializer(required=False)



    class Meta:
        model = Blogs
        fields = ('id','title','user','subtitle','subimage','created_at','updated_at')

class BlogsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user = BlogsUserSerializer(read_only = True)
    # subimage = UploadImagesSerializer()
    posts = PostSerializer(many=True,read_only = True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data=validated_data)
        pass

    class Meta:
        model = Blogs
        fields = ('id','title','user','content','subtitle','subimage','created_at','updated_at','posts')

class ReportsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Reports
        fields = ('user','blog','created_at','reason','permit')
        read_only_fields = ('user','permit')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data=validated_data)
        pass
