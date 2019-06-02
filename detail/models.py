from django.db import models

# Create your models here.
class Detail(models.Model):
    stt = models.CharField( max_length = 4)
    title = models.CharField( max_length = 1000)
    year = models.CharField( max_length = 10, null = True)
    rating =  models.CharField( max_length = 1000, null = True)
    subText = models.CharField( max_length = 1000,  null = True)
    link_poster = models.CharField( max_length = 1000,  null = True)
    linkVideoPoster = models.CharField( max_length = 1000,  null = True)
    linkVideoTrailer = models.CharField( max_length = 1000,  null = True)
    Storyline = models.CharField( max_length = 1000,  null = True)