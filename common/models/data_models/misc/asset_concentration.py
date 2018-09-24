from django.db import models

# 1	International Specialization
# 2	Agricultural Specialization
# 3	Credit-card Specialization
# 4	Commercial Lending Specialization
# 5	Mortgage Lending Specialization
# 6	Consumer Lending SpecializationI
# 7	Other Specialized < $1 Billion
# 8	All Other < $1 Billion
# 9	All Other > $1 Billion

class Asset_Concentration(models.Model):
    id = models.IntegerField(primary_key=True,db_column="id", verbose_name="ID")
    name = models.CharField(db_column="Name", max_length=67, verbose_name="Name")

    class Meta:
        managed = False
        db_table = "fdic_asset_concentrations"
        verbose_name = "Asset Concentration"
        ordering = ['id']

    def __str__(self):
        return self.name