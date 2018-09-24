from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Product Id")
    name = models.CharField(db_column="name", max_length=50, verbose_name="Name")
    description = models.CharField(db_column="description", max_length=255, verbose_name="Description", blank=True, null=True)
    is_active = models.BooleanField(db_column="is_active", verbose_name="Active", default=True)
    enable_trial = models.BooleanField(db_column="enable_trial", verbose_name="Enable for Trial")
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "system_products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name