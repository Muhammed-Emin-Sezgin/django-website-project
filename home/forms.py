from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='search', max_length=100)
    calismaSekli = forms.CharField(label='calismaSekli', max_length=20, required=False)

