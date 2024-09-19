from django import forms
from .models import Booking
from django.forms import TextInput, EmailField, Select, Textarea

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields=['name','email','phone','date','doc_name','department','message']
        widgets={
            'name':TextInput(
                attrs={
                    "name":"name",
                    "type":"text",
                    "placeholder":"Name"
                }
            ),
            'email':TextInput(
                attrs={
                    "name":"email",
                    "type":"email",
                    "placeholder":"Email"
                }
            ),
            'phone':TextInput(
                attrs={
                    "name":"phone",
                    "type":"text",
                    "placeholder":"Phone"
                }
            ),
            'doc_name':TextInput(
                attrs={
                    "name":"doc_name",
                    "type":"text",
                    "placeholder":"Doctor Name"
                }
            ),
            'date':TextInput(
                attrs={
                    "type":"text",
                    "placeholder":"Date",
                    "id":"datepicker"
                }
            ),
            'department':Select(
                attrs={

                }
            ),
            'messsage':Textarea(
                attrs={
                    "name":"message", 
                    "placeholder":"Write Your Message Here....."
                }
            )


        }