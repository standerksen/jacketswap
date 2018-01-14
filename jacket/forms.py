from django import forms
from .models import Jacket


class CreateJacketForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control js-input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control js-input'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control js-input'}))
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control js-input file-input'}))
    lost_found = forms.ChoiceField(choices={('lost', 'Lost'), ('found', 'Found')},
                                   widget=forms.RadioSelect(attrs={'class': 'radio-select'}),
                                   label="Lost or found")

    class Meta:
        model = Jacket
        fields = ['title', 'description', 'location', 'image', 'lost_found']
