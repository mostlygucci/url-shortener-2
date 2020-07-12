from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from .models import Link

_alias = Link._meta.get_field('alias')
_url = Link._meta.get_field('url')


class URLShortenerForm(forms.Form):

    alias = forms.CharField(
        max_length=_alias.max_length,
        required=False,
        help_text=_("An optional alias you want to generate. "
                    "One will be chosen automatically if you don't enter one."),
        label=_('CUSTOM SHORT LINK'),
        validators=[RegexValidator(
            regex=r'^[a-zA-Z0-9-_]+$',
            code='invalid_alias',
            message='Alias can only contain alphabets, numerals, underscores and hyphens',
        )]
    )

    url = forms.URLField(
        max_length=_url.max_length,
        required=True,
        help_text=_("The URL you want to shorten."),
        label=_('SHORTEN'),
        widget=forms.URLInput(
            attrs={'placeholder': 'YOUR LONG URL HERE',
                   'required': 'true'},
        ),
    )
