from django import forms
from django.core.exceptions import ValidationError
from .models import Flights, Tourists
import datetime
from pycountry import countries


class FlightsForm(forms.ModelForm):
    class Meta:
        model = Flights
        fields = "__all__"

    def clean(self):
        no_seats = self.cleaned_data.get('number_of_seats')
        passengers = self.cleaned_data.get('list_of_tourists')
        if no_seats and passengers.count() > no_seats:
            raise ValidationError('Maximum ' + str(no_seats) + ' passengers are allowed!')

        departure = self.cleaned_data.get('departure_time')
        arrival = self.cleaned_data.get('arrival_time')
        if departure and arrival < departure:
            raise ValidationError('Departure date cannot be later then the arrival date!'
                                  ' Please change the date and try again.')

        return self.cleaned_data


class TouristsForm(forms.ModelForm):
    class Meta:
        model = Tourists
        fields = "__all__"

    def clean(self):
        birthday = self.cleaned_data.get('date_of_birth')
        if birthday > datetime.date.today():
            raise ValidationError('Date of birth must be today or in the past!')

        flights = self.cleaned_data.get('list_of_flights')
        for flight in flights:
            if flight.number_of_seats > flight.list_of_tourists.count():
                raise ValidationError('Maximum ' + str(flight.number_of_seats) +
                                      ' passangers are allowed in the flight that launches on ' +
                                      str(flight.departure_time.date())+' at '+str(flight.departure_time.time()) +
                                      ' and lands on ' + str(flight.arrival_time.date()) +
                                      ' at '+str(flight.arrival_time.time()))

        country = self.cleaned_data.get('country')
        candidates=[]
        if country:
            for c in countries:
                if country.lower() in (c.name.lower(), c.alpha_2.lower(), c.alpha_3.lower()):
                    candidates.append(country)
        if not len(candidates):
            raise ValidationError('Invalid country name: ' + country)

        return self.cleaned_data
