from django.db import models


class Structure_Code(models.Model):
    code = models.IntegerField(primary_key=True, db_column="Code", verbose_name="Code")
    description = models.CharField(db_column="Description", max_length=67, verbose_name="Description")

    class Meta:
        managed = False
        db_table = "fdic_structure_codes"
        ordering = ['description']
        verbose_name = "Structure Code"

    def __str__(self):
        return self.description
