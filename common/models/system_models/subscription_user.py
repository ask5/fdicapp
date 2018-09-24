from django.db import models
from .subscription import Subscription
from django.contrib.auth.models import User


class Subscription_User(models.Model):
    id = models.AutoField(primary_key=True)
    sub_id = models.ForeignKey(Subscription, db_column="sub_id", on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "system_subscription_users"
        verbose_name = "Subscription User"
        verbose_name_plural = "Subscription Users"
