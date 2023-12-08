# sentiment_analysis_app/forms.py

from django import forms

class SearchForm(forms.Form):
    artist_name = forms.CharField(label='Artist Name', max_length=255)

class SearchRegion(forms.Form):
    region_name = forms.CharField(label='Region', max_length=255)
