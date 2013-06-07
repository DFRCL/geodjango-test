from django.views.generic import View
from django.shortcuts import render_to_response, RequestContext


class MapView(View):
    def get(self, request, *args, **kwargs):

        return render_to_response('google.html')
