from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import MapView
from app.api import GeoAPIView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^map/$', MapView.as_view(), name='home'),
    # url(r'^geogjango_demo/', include('geogjango_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', GeoAPIView.as_view(), name='geo-api-view')
)
