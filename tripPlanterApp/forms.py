from django import forms
from tripPlanterApp.models import Place

class MyForm(forms.Form):
    places = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,queryset=Place.objects.all())