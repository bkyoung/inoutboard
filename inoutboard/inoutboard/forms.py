from django import forms

class StatusUpdateForm(forms.Form):
    full_name = forms.CharField()
    status = forms.CharField(required=False)
    comment1 = forms.CharField(required=False)
    comment2 = forms.CharField(required=False)
    estimated_return = forms.CharField(required=False)
