from django import forms

class DateRangeForm(forms.Form):
    start = forms.DateField()
    end =  forms.DateField()