from django import forms
from tripPlanterApp.models import Place,Trip

class MyForm(forms.Form):
    places = forms.ModelMultipleChoiceField(required=True, queryset=Place.objects.all())

    # def __init__(self, *args, **kwargs):
    #     extra = kwargs.pop('extra')
    #     super(MyForm, self).__init__(*args, **kwargs)

class CreateTrip(forms.ModelForm):
    title = forms.CharField(max_length=128, required=True, help_text="Provide a title for your trip")
    #planner = forms.CharField(required=True, widget=forms.HiddenInput)

    class Meta:
        #Providing associated model
        model = Trip
        exclude=('picture','isSuggestedTrip','planner')