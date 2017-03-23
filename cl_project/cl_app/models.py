from django.db import models


class Posting(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=1500)
    image = models.CharField(max_length=100)
    # category = models.ForeignKey(null=True)
    city = models.CharField(max_length=20)
    # user = models.ForeignKey(null=True)


class Category(models.Model):
    name = models.CharField(max_length=20)
    # parent_category = models.ForeignKey(null=True)
