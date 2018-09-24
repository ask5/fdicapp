from django.db import models

class Memoranda(models.Model):

    class Meta:
        managed = False
        db_table = "financials_memoranda"
        verbose_name = "Memoranda"
        verbose_name_plural = "Memoranda"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    lnsb= models.IntegerField(db_column="lnsb",verbose_name="Outstanding principal balance of obligations transferred")
    lnsbr= models.IntegerField(db_column="lnsbr",verbose_name="Amount of retained recourse exposure")
    msrece= models.IntegerField(db_column="msrece",verbose_name="Outstanding Princiapl Balance of Assets Serviced for Others 1-4 Family Res. Mrtg")
    msrnrece= models.IntegerField(db_column="msrnrece",verbose_name="Outstanding Princiapl Balance of Assets Serviced for Others 1-4 Family Res. Mrtg")
    lnserv= models.IntegerField(db_column="lnserv",verbose_name="Outstanding Princiapl Balance of Assets Serviced for Others Other Fin. Assets")
    MSRESFCL= models.IntegerField(db_column="MSRESFCL",verbose_name="Serviced 1-4 family loans in foreclosure")
    abcxbk= models.IntegerField(db_column="abcxbk",verbose_name="Asset-Backed Commercial Paper Conduits Sponsored by the Bank")
    abcxoth= models.IntegerField(db_column="abcxoth",verbose_name="Asset-Backed Commercial Paper Conduits Sponsored by Other Unrelated Inst.")
    abcubk= models.IntegerField(db_column="abcubk",verbose_name="Unused Commitments to Provide Liquidity to Conduit Structures")
    abcuoth= models.IntegerField(db_column="abcuoth",verbose_name="Unused Commitments to Provide Liquidity, Unrelated Institutions")
    szcrcdfe= models.IntegerField(db_column="szcrcdfe",verbose_name="Outstanding Credit Card Fees and Financial Charges")
