from django.db import models

class Government_Obligations(models.Model):

    class Meta:
        managed = False
        db_table = "financials_government_obligations"
        verbose_name = "U.S. Government Obligations"
        verbose_name_plural = "U.S. Government Obligations"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")
    scage = models.BigIntegerField(db_column="scage",verbose_name="U.S. Government agency obligations")
    scaot = models.BigIntegerField(db_column="scaot",verbose_name="U.S. government agencies")
    scspn = models.BigIntegerField(db_column="scspn",verbose_name="Issued by U.S. government enterprises (GSEs)")
    scfmn = models.BigIntegerField(db_column="scfmn",verbose_name="Issued by F.N.M.A. and F.H.L.M.C.")
    scgnm = models.BigIntegerField(db_column="scgnm",verbose_name="Issued by G.N.M.A.")
    sccol = models.BigIntegerField(db_column="sccol",verbose_name="CMOs issued by government agencies or sponsored agencies")
    SCCPTG = models.BigIntegerField(db_column="SCCPTG",verbose_name="Commercial mortgage pass-through securities – FNMA, FHLMC, or GNMA")
    SCCMOG = models.BigIntegerField(db_column="SCCMOG",verbose_name="Other commercial MBS Issued or guaranteed by US Govrnmnt agencies or sponsored")
