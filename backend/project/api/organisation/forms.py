from django.forms import forms

from .models import Organisation


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Organisation
        widgets = {
            'yes_or_no': forms.RadioSelect
        }
