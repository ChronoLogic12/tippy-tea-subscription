from tkinter import Widget
from django import forms
from .models import Mailing


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ('email',)


    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['autofocus'] = True
        self.fields['email'].widget.attrs['required'] = True
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].label = False


class MassEmailForm(forms.Form):
    subject = forms.CharField(max_length=180 )
    message = forms.CharField(max_length=10000, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
            """
            Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'subject': 'Subject',
                'message': 'Message',
            }

            self.fields['subject'].widget.attrs['autofocus'] = True
            self.fields["message"].widget.attrs['class'] = 'materialize-textarea'
            for field in self.fields:
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False

