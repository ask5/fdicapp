from django.db import models


class Total_Debt_Securities(models.Model):

    class Meta:
        managed = False
        db_table = "financials_total_debt_securities"
        verbose_name = "Total Debt Securities"
        verbose_name_plural = "Total Debt Securities"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    scrdebt = models.BigIntegerField(db_column="scrdebt",verbose_name="Total debt securities")
    scpt3les = models.BigIntegerField(db_column="scpt3les",verbose_name="Three months or less")
    scpt3t12 = models.BigIntegerField(db_column="scpt3t12",verbose_name="Over three months through twelve months")
    scpt1t3 = models.BigIntegerField(db_column="scpt1t3",verbose_name="Over one year through three years")
    scpt3t5 = models.BigIntegerField(db_column="scpt3t5",verbose_name="Over three years through five years")
    scpt5t15 = models.BigIntegerField(db_column="scpt5t15",verbose_name="Over five years through fifteen years")
    scptov15 = models.BigIntegerField(db_column="scptov15",verbose_name="Over fifteen years")
    sco3yles = models.BigIntegerField(db_column="sco3yles",verbose_name="Three years or less")
    scoov3y = models.BigIntegerField(db_column="scoov3y",verbose_name="Over three years")
    scnm3les = models.BigIntegerField(db_column="scnm3les",verbose_name="Three months or less")
    scnm3t12 = models.BigIntegerField(db_column="scnm3t12",verbose_name="Over three months through twelve months")
    scnm1t3 = models.BigIntegerField(db_column="scnm1t3",verbose_name="Over one year through three years")
    scnm3t5 = models.BigIntegerField(db_column="scnm3t5",verbose_name="Over three years through five years")
    scnm5t15 = models.BigIntegerField(db_column="scnm5t15",verbose_name="Over five years through fifteen years")
    scnmov15 = models.BigIntegerField(db_column="scnmov15",verbose_name="Over fifteen years")
    sc1les = models.BigIntegerField(db_column="sc1les",verbose_name="With remaining maturity of one year or less")