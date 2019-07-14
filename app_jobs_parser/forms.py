from django import forms

class input_form(forms.Form):
    position = forms.CharField(label='Position', max_length=100)
    location = forms.CharField(label='Location', max_length=100)

    def clean(self):
         cleaned_data = super(input_form, self).clean()
         position = cleaned_data['position']
         location = cleaned_data['location']
         if not position and not location:
            raise forms.ValidationError('You have to write something!')
