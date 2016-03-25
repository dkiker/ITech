from django import forms
from tripPlanterApp.models import Place,Trip

#Forms "MyForm" and "CreateTrip" help in creating individual trips.
class MyForm(forms.Form):
    places = forms.ModelMultipleChoiceField(required=True, queryset=Place.objects.all())

class CreateTrip(forms.ModelForm):
    title = forms.CharField(max_length=128, required=True, help_text="Provide a title for your trip")
    class Meta:
        #Providing associated model
        model = Trip
        exclude=('photograph','isSuggestedTrip','planner')