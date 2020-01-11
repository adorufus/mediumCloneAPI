from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return self.name
    

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    thumbnail = models.CharField(max_length=255, default='https:/test.com/goblok.png')
    Author = models.ForeignKey('Author', related_name='articles', on_delete=models.PROTECT)
    def __str__(self):
        return self.title

class ArticleDetail(models.Model):
    id = models.AutoField(primary_key=True)
    Article = models.ForeignKey('Article', on_delete=models.PROTECT)
    