from django.db import models
from django.contrib.auth.models import User
from monolith.constant import NORMALIZED_STRINGS, CONSTANT
from monolith.strings import STR_MALE, STR_FEMALE, STR_NOT_INFORMED, STR_AVERAGE_JOE, STR_ATHLETE


# Create your models here.
class Profile(models.Model):
    MALE = 'MA'
    FEMALE = 'FE'
    NOT_INFORMED = 'NF'

    AVERAGE_JOE = 'AJ'
    ATHLETE = 'AT'

    GENDER_CHOICES = [
        (MALE, STR_MALE),
        (FEMALE, STR_FEMALE),
        (NOT_INFORMED, STR_NOT_INFORMED),
    ]

    CONDITION_CHOICES = [
        (AVERAGE_JOE, STR_AVERAGE_JOE),
        (ATHLETE, STR_ATHLETE),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    gender = models.CharField(
        max_length=NORMALIZED_STRINGS['CHOICES'],
        choices=GENDER_CHOICES,
    )
    condition = models.CharField(
        max_length=NORMALIZED_STRINGS['CHOICES'],
        choices=CONDITION_CHOICES,
    )

    def __str__(self):
        return f"{self.user.get_full_name()}"


class HistoricBmi(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bmi = models.DecimalField(**CONSTANT['BMI'])

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.date} - {self.bmi}"