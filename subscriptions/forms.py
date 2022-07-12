from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = '__all__'
        widgets = {
            'description': forms.Textarea,
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'description': 'Description',
            'price': 'Price',
            'weight': 'Weight',
            'image_url': 'Image URL',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == "description":
                self.fields["description"].widget.attrs['class'] = 'materialize-textarea'
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False