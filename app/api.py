import json
from rest_framework.views import APIView
from rest_framework.response import Response
from vectorformats.Formats import Django, GeoJSON
from app.models import Venue

class GeoAPIView(APIView):

    def get(self, *args, **kwargs):
        """
        Returns data in GeoJSON format ready to be consumed by a mapping system
        """
        queryset = Venue.objects.filter(city__icontains="toronto")

        django_formatter = Django.Django(
            geodjango="coordinates",
            properties=['name', 'city', 'state'])
        geojson_formatter = GeoJSON.GeoJSON()
        data = json.loads(geojson_formatter.encode(django_formatter.decode(queryset)))

        return Response(data)
