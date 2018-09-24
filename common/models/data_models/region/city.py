from django.db import models
from .state import State


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column="Name", max_length=50, verbose_name="Name")
    state = models.ForeignKey(State,
                              on_delete=models.DO_NOTHING,
                              db_column="state",
                              verbose_name="State")

    class Meta:
        managed = False
        db_table = "fdic_cities"
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name