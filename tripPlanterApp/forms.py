from django import forms
from tripPlanterApp.models import Place

class MyForm(forms.Form):
    places = forms.ModelMultipleChoiceField(required=True, queryset=Place.objects.all())

    # def __init__(self, *args, **kwargs):
    #     extra = kwargs.pop('extra')
    #     super(MyForm, self).__init__(*args, **kwargs)

