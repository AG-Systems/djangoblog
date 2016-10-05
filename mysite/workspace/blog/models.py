from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=140)
    desc = models.CharField(max_length=140)
    content = models.TextField()
    slug = models.SlugField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    link = models.URLField(blank=True)
    link_desc = models.CharField(max_length=140, blank=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog.views.getpost', args=[self.slug])
    