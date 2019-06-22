# for creating and manipulating models
from django.db import models
#for loading a translation of a string (Unicode support) in a lazy fashion
from django.utils.translation import ugettext_lazy as _
#for admin account
from django.contrib.auth.models import User


class Flights(models.Model):
    """
    Model of filght: array of flights
    """

    departure_time = models.DateTimeField(_('departure date'))
    arrival_time = models.DateTimeField(_('arrival date'))
    number_of_seats = models.PositiveSmallIntegerField(default=0,
                                                        help_text="Type the number of avaliable seats in this flight.")
    ticket_price = models.PositiveIntegerField(default=0, help_text="Type the price for the ticket.")
    list_of_tourists = models.ManyToManyField('Tourists', related_name='tourists', blank=True)

    def __str__(self):
        return 'Flight launch: %s  landing: %s' % (str(self.departure_time.date())+" at "+ str(self.departure_time.time()),
                                                   str(self.arrival_time.date())+" at "+ str(self.arrival_time.time()))

    class Meta:
        ordering = ['departure_time', 'arrival_time']
        verbose_name = _('Flight')
        verbose_name_plural = _('Flights')


class Tourists(models.Model):
    """
    Model of tourists: array of tourists
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = models.CharField(_('First name'), max_length=250)
    last_name = models.CharField(_('Last name'), max_length=250)
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES, help_text="Choose the gender: ")
    country = models.CharField(_('Country'), max_length=250)
    remarks = models.TextField(_('Remarks'), blank=True, help_text="Type remarks: ")
    date_of_birth = models.DateField(_('Date of birth'))
    list_of_flights = models.ManyToManyField('Flights', related_name='flights', blank=True)

    def __str__(self):
        return '%s %s d.o.b. %s' % (self.first_name, self.last_name, (str(self.date_of_birth)))

    class Meta:
        ordering = ['first_name', 'last_name', 'date_of_birth']
        verbose_name = ('Tourist')
        verbose_name_plural = ('Tourists')