from django import forms

from .models import Booking,Feedback


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput,
        }

        labels = {
            'p_name' : "Patient Name: ", 
            'p_phone' : "Patient Phoneno: ",
            'p_email' : "Patient EmailID: ", 
            'doc_name' : "Doctor Name: ",
            'booking_date' : "Booking Date: ", 
        }
    
class Feedbackform(forms.ModelForm):
    class Meta:
        model =Feedback
        fields = ['f_name','f_email','f_message']

        labels = {
            'f_name' : "Your Name: ", 
            'f_email' : "Your Email: ", 
            'f_message' : "Your Message: ", 

        }