import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.IntegerField(validators=[
            MaxValueValidator(9),
            MinValueValidator(1)
        ])
    date = models.TextField(max_length=8)
    value = models.TextField(max_length=10)
    cpf = models.TextField(max_length=11)
    credit_card = models.TextField(max_length=12)
    hour = models.TextField(max_length=6)
    owner = models.TextField(max_length=14)
    name = models.TextField(max_length=19)