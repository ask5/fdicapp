from django.db import models
from .customer import Customer

class ContactPerson(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Contact Id")
    customer_id = models.ForeignKey(Customer, db_column="customer_id", on_delete=models.DO_NOTHING)
    first_name = models.CharField(db_column="first_name", max_length=30, verbose_name="First Name")
    last_name = models.CharField(db_column="last_name", max_length=150, verbose_name="Last Name")
    phone = models.CharField(db_column="phone", max_length=50, verbose_name="Phone Number(s)", blank=True, null=True)
    email = models.CharField(db_column="email", max_length=254, verbose_name="Email", blank=True, null=True)
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "system_contacts"
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)