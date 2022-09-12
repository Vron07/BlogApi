from re import L
from .serializers import *

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (ListCreateAPIView,
                                    RetrieveAPIView,
                                    RetrieveUpdateDestroyAPIView,
                                    ListAPIView)

from .permissions import IsOwnerOrReadOnly

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework.pagination import PageNumberPagination

from rest_framework.mixins import (ListModelMixin,CreateModelMixin,
                                   RetrieveModelMixin,UpdateModelMixin,
                                   DestroyModelMixin)
from .paginations import CustomPagination

######################################
#            COMMENT                 #
######################################

# Generic APIView
# class CommentList(ListCreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
                        

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# class CommentDetail(RetrieveAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]

# API Views COMMENT
class CommentList(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    
    def get(self,request,format = None):
        account = Comment.objects.all()
        serializer = CommentSerializer(account,many = True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self,request,pk,format = None):
        account = self.get_object(pk)
        serializer = CommentSerializer(account)
        return Response(serializer.data)

    def put(self,request,pk,format = None):
        account = self.get_object(pk)
        serializer = CommentSerializer(account,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

######################################
#              POST                  #
######################################

# class PostList(ListCreateAPIView):
#     queryset = Post.objects.all()    
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class PostList1(ListAPIView):
    queryset = Post.objects.all()    
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    pagination_class = CustomPagination

# class PostDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)

# API Views POST
class PostList(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def get(self,request,format = None):
        account = Post.objects.all()
        serializer = PostSerializer(account,many = True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self,request,pk,format = None):
        account = self.get_object(pk)
        serializer = PostSerializer(account)
        return Response(serializer.data)

    def put(self,request,pk,format = None):
        account = self.get_object(pk)
        serializer = PostSerializer(account,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
######################################
#               REPLY               #
######################################

# class ReplyList(ListCreateAPIView):
#     queryset = Reply.objects.all()
#     serializer_class = ReplySerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# API Views REPLY
class ReplyList(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]


    def get(self,request,format = None):
        account = Reply.objects.all()
        serializer = ReplySerializer(account,many = True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ReplySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)