from django.db import models


class FeatureTags(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    tag = models.CharField(db_column="tag", max_length=50, verbose_name="Tag", help_text="A unique aplha-numeric code to "
                                                                                         "identify the feature ")
    name = models.CharField(db_column="name", max_length=128, verbose_name="Name")
    description = models.CharField(db_column="description", max_length=255, verbose_name="Description", blank=True,
                                   null=True)
    is_active = models.BooleanField(db_column="is_active", verbose_name="Active", default=True)
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "system_feature_tags"
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return "{}-{}".format(self.tag, self.name)