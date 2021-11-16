from django.db import models

# Create your models here.


class Advertiser(models.Model):
    advertiser_name=models.CharField(max_length=50)

class Channel(models.Model):
    channel_name = models.CharField(max_length=50)
    advertiser=models.ForeignKey(Advertiser, on_delete=models.CASCADE)
    


