from django import forms

# Create your forms here.

class ExampleForm(forms.Form):
    guess = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':20 , 'required': True}))