from django.db import models

class camp(models.Model):
   event_name = models.CharField(max_length=100)
   date = models.CharField(max_length=100)
   time = models.CharField(max_length=10)
   location = models.CharField(max_length=10,default='')
   is_liked = models.BooleanField(default=0)
   img = models.ImageField(upload_to='pictures')

   def __str__(self):
      return self.title

