from django.db import models

class MSA(models.Model):
    code = models.IntegerField(primary_key=True, db_column="code", verbose_name="Code")
    name = models.CharField(db_column="name", max_length=75, verbose_name="Name")

    class Meta:
        managed = False
        db_table = "fdic_msa"
        verbose_name = "MSA"
        ordering = ['name']

    def __str__(self):
        return self.name