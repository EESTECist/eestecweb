from django.db import models
from datetime import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

#    @models.permalink
    def get_absolute_url(self):
        pass
#        return ('blog_post_detail', (),
#               {
#                    'slug' :self.slug,
#               })
