from django import forms
from GhostTown.models import BoastRoast

class BoastRoastForm(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = ["choices", "user_input"]