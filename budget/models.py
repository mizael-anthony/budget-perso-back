import datetime
from django.db.models.fields import DateField
from personnal.settings import DEFAULT_IMAGE
from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.



class Action(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=False)

    category = models.CharField(
        max_length=20,
        null=False,
        choices=[('charge', 'Charge'),('produit', 'Produit')])
    
    logo = models.FileField(
        upload_to='img/',
        null=True,
        default=DEFAULT_IMAGE)



    def __str__(self)->str:
        return self.name






class Journal(models.Model):
    date = models.DateField(
        default=datetime.date.today)

    action = models.ForeignKey(
        "Action",
        related_name="journals",
        on_delete=CASCADE,
        null=True
    )

    cost = models.IntegerField()


    def __str__(self) -> str:
        return self.action.__str__()



