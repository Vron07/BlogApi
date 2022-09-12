from django.db import models
from account.models import User

# Create your models here.

class Post(models.Model):
    postName = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    title = models.CharField(max_length=100,blank=False,default='Headline')
    subtitle = models.CharField(max_length=100,blank=True,default='')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, default='')

    def __str__(self):
        return self.postName

    @property
    def comments(self):
        return self.comment_set.all()

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    
    @property
    def replys(self):
        return self.reply_set.all()

    def __str__(self):
        return self.content

class Reply(models.Model):
    comment = models.ForeignKey('Comment',on_delete=models.CASCADE , related_name='replys')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.content