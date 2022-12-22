from django.db import models


# Create your models here.
class Plants(models.Model):
    pcod = models.CharField(max_length=30)
    pname = models.CharField(max_length=100)
    pcat = models.CharField(max_length=50)
    rate = models.IntegerField()
    img = models.ImageField(upload_to='pic')

    def __str__(self):
        return self.pname