from django import forms
from scraping.models import City, Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        to_field_name="name",
        required=False)
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        to_field_name="name",
        required=False)
