from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Customer Id")
    name = models.CharField(db_column="name", max_length=128, verbose_name="Customer Name")
    description = models.TextField(db_column="description", max_length=500, verbose_name="Business Description", blank=True, null=True)
    address1 = models.CharField(db_column="address1", max_length=50, verbose_name="Address Line 1")
    address2 = models.CharField(db_column="address2", max_length=50, verbose_name="Address Line 2", blank=True, null=True)
    city = models.CharField(db_column="city", max_length=50, verbose_name="City")
    state = models.CharField(db_column="state", max_length=25, verbose_name="State")
    zip = models.CharField(db_column="zip", max_length=10, verbose_name="Zip Code")
    country = models.CharField(db_column="country", max_length=25, verbose_name="Country")
    phone = models.CharField(db_column="phone", max_length=20, verbose_name="Phone", blank=True, null=True)
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified", blank=True, null=True)
    is_active = models.BooleanField(db_column="is_active", verbose_name="Active", default=True)

    class Meta:
        managed = False
        db_table = "system_customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name