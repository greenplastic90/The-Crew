from .models import Crew
from django import forms

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['name', 'members']

    def clean_members(self):
        members = self.cleaned_data.get('members')
        if members and len(members) < 2:
            raise forms.ValidationError('At least two members are required.')
        return members