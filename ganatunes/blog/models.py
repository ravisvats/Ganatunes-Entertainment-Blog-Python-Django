from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField



    def get_absolute_url(self):
            return reverse('home')

class Post(models.Model):
    title = models.TextField(max_length=250)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.TextField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body=models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.TextField(max_length=250, default='coding')
    snippet = models.CharField(max_length=255,)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)
    def get_absolute_url(self):
        #return reverse('article_detail', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
