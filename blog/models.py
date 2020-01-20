from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Category(models.Model):
    name = models.CharField(max_length=50)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()
    image = models.ImageField(upload_to='images/', blank=True)
    pub_date = models.DateField()
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    @property
    def formatted_markdown(self):
        return markdownify(self.body)
    
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')