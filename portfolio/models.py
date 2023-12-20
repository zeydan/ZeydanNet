from django.db import models
from django.utils.text import slugify
# Create your models here.

class Portfolio(models.Model):
    title = models.CharField(max_length=50, null=False)
    unique_title = models.CharField(max_length=50, null=False, blank=True, unique=True, db_index=True)
    labels = models.CharField(max_length=100)
    cover_image = models.CharField(max_length=100, null=False)
    images = models.JSONField(max_length=200)
    content = models.TextField(null=False)
    time = models.DateTimeField(null=False)
    visible = models.BooleanField()
    index = models.BooleanField()
    sort_id = models.IntegerField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.unique_title = slugify(self.title)
        super().save(*args, **kwargs)

class PortfolioFilter(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name