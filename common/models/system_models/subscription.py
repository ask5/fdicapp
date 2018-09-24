from django.db import models
from .customer import Customer
from common.util import random_number


class Subscription(models.Model):
    sub_id = models.CharField(primary_key=True, max_length=15, db_column="sub_id", default=random_number, unique=True,
                              verbose_name="Subscription Id")
    customer_id = models.ForeignKey(Customer, db_column="customer_id", on_delete=models.DO_NOTHING)
    note = models.TextField(db_column="note", max_length=500, verbose_name="Notes",
                                   blank=True, null=True)
    is_active = models.BooleanField(db_column="is_active", verbose_name="Active", default=True)
    is_trial = models.BooleanField(db_column="is_trial", verbose_name="Trial")
    start_date = models.DateTimeField(db_column="start_date", verbose_name="Start Date")
    end_date = models.DateTimeField(db_column="end_date", verbose_name="End Date")
    auto_renew = models.BooleanField(db_column="auto_renew", verbose_name="Auto Renew", default=False)
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "system_subscriptions"
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
