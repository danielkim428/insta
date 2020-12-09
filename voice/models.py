from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    content = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name

class Current(models.Model):
    num = models.IntegerField()

    def __str__(self):
        return str(self.num)
