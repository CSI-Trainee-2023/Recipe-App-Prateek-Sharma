from django import forms
from .models import CreateRecipe


class Createrecipe(forms.ModelForm):

    class Meta:
        model = CreateRecipe
        fields = ('Name','Detail','Date')