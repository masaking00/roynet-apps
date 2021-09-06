from django import forms
from django.forms import fields, models
from django import forms

from report.models import FoundItems

class FoundItemUpdateForm(forms.ModelForm):
    files = forms.FileField(widget=forms.FileInput)

    class Meta:
        model = FoundItems
        fields = ("files","create_user","create_date","memo")

class FoundItemsForm(forms.ModelForm):
    class Meta:
        model = FoundItems
        fields = ("hotels","FoundItems_Year","FoundItems_Month","files","create_user","create_date","memo")
