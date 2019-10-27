from django.db import models
from utils.basemodel import BaseModel


# Create your models here.

class Article(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("User",on_delete=models.DO_NOTHING)
    show_nums = models.IntegerField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,related_name="articles")
    comment_nums = models.IntegerField()


class Category(BaseModel):
    name = models.CharField(max_length=50)
