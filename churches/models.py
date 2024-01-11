from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    order = models.PositiveSmallIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
