from django.db import models
# Posts models
from django.contrib.auth.models import User
STATUS = ((0,"Draft"),(1,"Publish"))

class Post(models.Model):
    title = models.CharField(max_length = 200,unique = True)
    slug = models.SlugField(max_length = 200,unique = True) 
    author = models.CharField(max_length=100,default = "Admin")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices= STATUS,default=0)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="author")
    text = models.TextField(help_text="Comments")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
