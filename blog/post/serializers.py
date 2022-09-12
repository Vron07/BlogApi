
from rest_framework import serializers
from .models import Post,Comment, Reply

from account.models import *

######################################
#              REPLY                 #
######################################
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

######################################
#            COMMENT                 #
######################################
class CommentSerializer(serializers.ModelSerializer):

    replys = ReplySerializer(many=True,read_only = True)  

    class Meta:
        model = Comment
        fields = ['post','created','content','replys']

    # def create(self, validated_data):
    #     replys=validated_data.pop('replys')
    #     comment = Post.objects.create(**validated_data)
    #     for reply in replys:
    #         Reply.objects.create(**comment,reply=reply)
    #     return comment

######################################
#              POST                  #
######################################
class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Post
        fields = ['postName','title','subtitle','created','content','comments']


    # def create(self, validated_data):
    #     comments=validated_data.pop('comments')
    #     post = Post.objects.create(**validated_data)
    #     for comment in comments:
    #         Comment.objects.create(**comment,post=post)
    #     return post