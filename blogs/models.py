from django.db import models

# Modelo del sitio.


class Blog (models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

class Category (models.Model):
    name = models.CharField(max_length=150)

    def __unicode__(self):
        return self.name

class Post (models.Model):

    title =models.CharField(max_length=150)
    abstract = models.CharField(max_length=500)
    body = models.CharField(max_length=1024)
    imageurl = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.title
