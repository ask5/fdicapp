from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):

    TYPES = (
        ('INS', 'Institution'),
        ('OFF', 'Office'),
        ('FAL', 'Financial Assets & Liabilities'),
    )

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, db_column="user_id", on_delete=models.DO_NOTHING)
    object_type = models.CharField(db_column="type", max_length=3, choices=TYPES, verbose_name="Object Type")
    cert = models.IntegerField(db_column="cert", verbose_name="Institution Cert")
    office_uninum = models.IntegerField(db_column="cert", verbose_name="Institution Cert", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "fdic_user_favorites"
        verbose_name = "User Favorites"
