from django import forms
from .models import Booking
class   Dateset(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = '__all__'
    widgets={
        'pdate': Dateset(),
    }

