from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def height_custom_validator(value):
    raise ValidationError(
        _('Invalid value: %(value)s'),
        params={'value': value},
    )


def weight_custom_validator(value):
    print(value)
    return True