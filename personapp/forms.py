from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields =('image','name','mobile','email','address')

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

