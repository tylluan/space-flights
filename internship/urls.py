"""
internship URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from spacecruise import views
from rest_framework import routers
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

#Resource routing for quick declaration of all the common routes for a given resourceful controller.
#wiring view logic to a set of URLs
router = routers.DefaultRouter()
router.register(r'tourists', views.TouristsViewSet)
router.register(r'flights', views.FlightsViewSet)


admin.site.unregister(User)
admin.site.unregister(Group)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('spacecruise.urls')),
    url(r'^$', views.index, name='index'),

]
