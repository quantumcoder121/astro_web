from django import forms

# creating a form
class InputForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    email_id = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Email ID"
        })
    )
    rating = forms.CharField(
        max_length=1,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Rate Me!"
        })
    )
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
