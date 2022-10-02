from django.contrib.gis.db import models


class Venue(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    coordinates = models.PointField(null=True, geography=False)

    objects = models.GeoManager()

    def __unicode__(self):
        return "%s, %s" % (self.name, self.city)


class Area(models.Model):
    name = models.CharField(max_length=100)
    area = models.PolygonField()

    def __unicode__(self):
        return self.name
