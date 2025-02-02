from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지')
    context = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일')
    view_count = models.IntegerField(verbose_name='조회수')