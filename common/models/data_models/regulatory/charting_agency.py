from django.db import models


class Charting_Agency(models.Model):
    code = models.CharField(primary_key=True, db_column="code", verbose_name="Code", max_length=10)
    name = models.CharField(db_column="name", max_length=50, verbose_name="Name")
    description = models.CharField(db_column="description", max_length=255, verbose_name="Description")

    class Meta:
        managed = False
        db_table = "fdic_charting_agencies"
        ordering = ['name']
        verbose_name = "Charter Agency"
        verbose_name_plural = "Charter Agencies"

    def __str__(self):
        return self.name