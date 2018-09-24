from django.db import models


class Regulator(models.Model):
    code = models.CharField(primary_key=True, db_column="code", verbose_name="Code", max_length=10)
    name = models.CharField(db_column="Name", max_length=50, verbose_name="Name")
    description = models.CharField(db_column="Description", max_length=255, verbose_name="Description")

    class Meta:
        managed = False
        db_table = "fdic_regulators"
        ordering = ['name']
        verbose_name = "Regulator"


    def __str__(self):
        return self.name