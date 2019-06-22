from spacecruise.models import Flights, Tourists
from rest_framework import viewsets
from .serializers import FlightsSerializer, TouristsSerializer
from rest_framework.views import APIView
from django.shortcuts import render


class IndexView(APIView):
    """
    API view for searching Recipes
    """
    allowed_methods = ['GET']
    serializer_class = FlightsSerializer


class FlightsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows flights to be viewed or edited.
    """
    queryset = Flights.objects.all()
    serializer_class = FlightsSerializer


class TouristsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tourists to be viewed or edited.
    """
    queryset = Tourists.objects.all().order_by('last_name')
    serializer_class = TouristsSerializer


def index(request):
    return render(request, 'index.html')