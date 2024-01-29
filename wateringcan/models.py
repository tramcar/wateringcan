from django.db import models

import markdown


class Page(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    content_html = models.TextField()
    slug = models.SlugField(max_length=50, unique=True)
    order = models.PositiveSmallIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # TODO: Sanitize markdown
        self.content_html = markdown.markdown(self.content)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
