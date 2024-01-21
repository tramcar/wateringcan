from django import forms


class ContactUsForm(forms.Form):
    sender = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Your e-mail address"
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control"}),
        label="Your message"
    )