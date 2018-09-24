from django.db import models
from django.contrib.auth.models import User


###
# User settings may go here
###
class UserDetail(models.Model):
    user = models.OneToOneField(User, primary_key=True, db_column="user_id", on_delete=models.CASCADE)
    department = models.CharField(max_length=100, db_column="department", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "auth_user_details"
        verbose_name = "User Detail"
