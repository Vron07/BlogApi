from django.urls import path
from .views import * 

urlpatterns = [
    path('posts/', PostList.as_view(),name='posts'),
    path('posts1/', PostList1.as_view(),name='posts1'),
    path('posts/<int:pk>/', PostDetail.as_view(),name='postdetail'),
    path('posts/self/', PostListSelf.as_view(),name='postsearch'),
    path('comments/', CommentList.as_view(),name='comments'),
    path('comments/<int:pk>/', CommentDetail.as_view(),name='commentdetail'),
    path('reply/', ReplyList.as_view(),name='replies'),
    path('reply/self/', ReplyListSelf.as_view(),name='replysearch'),
]
