from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from model_utils import Choices



class Baby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    birth_time = models.TimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = _("Baby")
        verbose_name_plural = _("Babies")

    def __str__(self):
        return self.user.username + ": " + self.name



class AbstractRegistration(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

    class Meta:
        abstract = True  

# ------------------------------------------------------------------------------------------------------------------------------

BREAST_SIDE_CHOICES = Choices(
    ("LEFT", _("Left")),
    ("RIGHT", _("Right")),
)

class BreastfeedRegistration(AbstractRegistration):
    breast_side = models.CharField(choices=BREAST_SIDE_CHOICES, max_length=30)

    class Meta:
        verbose_name = _("Breastfeed Registration")
        verbose_name_plural = _("Breastfeed Registrations")



class FoodRegistration(AbstractRegistration):
    ...

    class Meta:
        verbose_name = _("Food Registration")
        verbose_name_plural = _("Food Registrations")


class ContractionRegistration(AbstractRegistration):
    pain_measurement = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = _("Contaction Registration")
        verbose_name_plural = _("Contaction Registrations")


class DiaperRegistration(AbstractRegistration):
    ...

    class Meta:
        verbose_name = _("Diaper Registration")
        verbose_name_plural = _("Diaper Registrations")
# ------------------------------------------------------------------------------------------------------------------------------

class Measurement(AbstractRegistration):
    weight = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.weight and not self.length:
            raise ValidationError(_("Please, fill in atleast one measurement"))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Measurement")
        verbose_name_plural = _("Measurements")