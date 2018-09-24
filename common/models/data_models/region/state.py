from django.db import models


class State(models.Model):
    name = models.CharField(db_column="Name", max_length=50, verbose_name="Name")
    abbreviation = models.CharField(primary_key=True, db_column="Abbr",
                                    max_length=2, verbose_name="Abbreviation")
    type = models.CharField(db_column="Type", max_length=50, verbose_name="Type")

    class Meta:
        managed = False
        db_table = "fdic_states"
        ordering = ['name']
        verbose_name = "State"

    def __str__(self):
        return self.name