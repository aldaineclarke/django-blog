from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PostManager(models.Manager):
    def create_post(self, title, body):
        post = self.create(title = title, body = body)
        return post

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="post title")
    body = models.TextField(verbose_name="post content")
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name="author",blank=True, null=True)

    objects = PostManager()

    # class Meta:
    #     order_by = date_posted

    def __str__(self):
        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="post")
    comment = models.TextField(verbose_name="comment")
    date_created = models.DateTimeField(default=timezone.now)
    flag = models.BooleanField(default=False)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="commenter",blank=True, null=True)


    def __str__(self):
        return f"comments on {self.post.title}"

    


