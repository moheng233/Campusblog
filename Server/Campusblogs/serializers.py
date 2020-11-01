from Campusblog.fields import Base64ImageField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, Serializer

from Campusblogs.models import Blogs, Posts


class BlogsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'last_name')
        
class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user = BlogsUserSerializer(read_only = True)


    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data=validated_data)
        pass
    class Meta:
        model = Posts
        fields = ('id','user','content','created_at')



class BlogsListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    subimage = Base64ImageField()
    user = BlogsUserSerializer()



    class Meta:
        model = Blogs
        fields = ('id','title','user','subtitle','subimage','created_at','updated_at')

class BlogsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    user = BlogsUserSerializer(read_only = True)
    subimage = Base64ImageField()
    posts = PostSerializer(many=True,read_only = True)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user

        return super().create(validated_data=validated_data)
        pass

    class Meta:
        model = Blogs
        fields = ('id','title','user','content','subtitle','subimage','created_at','updated_at','posts')
