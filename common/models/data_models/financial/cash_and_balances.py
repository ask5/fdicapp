from django.db import models


class Cash_And_Balances(models.Model):

    class Meta:
        managed = False
        db_table = "financials_cash_and_balances"
        verbose_name = "Cash & Balances Due"
        verbose_name_plural = "Cash & Balances Due"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    chbal = models.BigIntegerField(db_column="chbal",verbose_name="Cash & Balances due from depository institutions")
    chcic = models.BigIntegerField(db_column="chcic",verbose_name="Cash items in process of collection")
    chitem = models.BigIntegerField(db_column="chitem",verbose_name="Collection in domestic offices")
    chcoin = models.BigIntegerField(db_column="chcoin",verbose_name="Currency and coin in domestic offices")
    chus = models.BigIntegerField(db_column="chus",verbose_name="Balances due from depository institutions in U.S.")
    chusfbk = models.BigIntegerField(db_column="chusfbk",verbose_name="U.S. branches of foreign banks")
    chnus = models.BigIntegerField(db_column="chnus",verbose_name="Balances due from foreign banks")
    chnusfbk = models.BigIntegerField(db_column="chnusfbk",verbose_name="Foreign branches of U.S. banks")
    chfrb = models.BigIntegerField(db_column="chfrb",verbose_name="Balances due from FRB")
    chbalni = models.BigIntegerField(db_column="chbalni",verbose_name="Total noninterest-bearing balances")
