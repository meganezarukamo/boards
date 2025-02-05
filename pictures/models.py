from datetime import timezone
from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to="img_list", blank=True, null=True)
    title = models.CharField(max_length=32)
    link = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
