from django.db import models
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """ Reservation Model Definition """
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled")
    )
