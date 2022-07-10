from django import forms
from .models import Profile
from django.utils.safestring import mark_safe

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields='__all__'
        exclude = ('user',)
        

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields: 
            if field == "country":
                self.fields["country"].widget.attrs['class'] = 'input-field col s12'
            if field not in ["country", "mailing"]:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            if field != "mailing":
                self.fields[field].label = False
            else:
                self.fields[field].label = mark_safe('<span>Subscribe to Newsletter</span>')
