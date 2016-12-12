from __future__ import unicode_literals

from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class UrlShort(models.Model):
    url = models.CharField(max_length=150)
    short = models.CharField(max_length=150, null=True, blank=True)
    image = models.FileField(upload_to='images')
    title = models.CharField(max_length=250)
    discription = models.CharField(max_length=500)
    created = models.DateTimeField()

    def __unicode__(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
            self.short = my_random_string()
        super(UrlShort, self).save(*args, **kwargs)


def my_random_string(string_length=4):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    random = random[0:string_length] # Return the random string.
    if UrlShort.objects.filter(short=random):
    	return my_random_string()
    else:
    	return random