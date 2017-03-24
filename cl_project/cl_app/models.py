from django.db import models


class Posting(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=1500)
    image = models.CharField(max_length=100)
    category = models.ForeignKey('Category', null=True, blank=True)
    city = models.CharField(max_length=20)
    # user = models.ForeignKey('User', null=True)
    posted_date = models.DateTimeField()

    def __str__(self):
        return self.title + str(self.posted_date)


class Category(models.Model):
    name = models.CharField(max_length=20)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.name
