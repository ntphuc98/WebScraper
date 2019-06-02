from django.db import models

# Create your models here.
class Movie(models.Model):
    mv_stt = models.CharField( max_length = 4)
    mv_name = models.CharField( max_length = 1000)
    mv_year = models.CharField( max_length = 1000)
    mv_rating = models.CharField( max_length = 1000, null = True)
    mv_link_detail = models.CharField( max_length = 1000)
    mv_link_poster = models.CharField( max_length = 1000)