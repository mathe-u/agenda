"""Forms"""

from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        """Meta Class ContactForm"""
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
        )

        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe',
        #             'placeholder': 'Escreva aqui',
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Messagem de erro',
        #         code='invalid'
        #     )
        # )

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Nao digite abc',
                    code='invalid',
                )
            )

        return first_name
