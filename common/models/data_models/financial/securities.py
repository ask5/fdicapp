from django.db import models

class Securities(models.Model):

    class Meta:
        managed = False
        db_table = "financials_securities"
        verbose_name = "Securities"
        verbose_name_plural = "Securities"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    sc = models.IntegerField(db_column="sc",verbose_name="Total securities")
    scus = models.IntegerField(db_column="scus",verbose_name="U.S. Government securities")
    scust = models.IntegerField(db_column="scust",verbose_name="U.S. Treasury securities")
    scage = models.IntegerField(db_column="scage",verbose_name="U.S. Government agency obligations")
    scmuni = models.IntegerField(db_column="scmuni",verbose_name="Securities issued by states & political subdivisions")
    scdomo = models.IntegerField(db_column="scdomo",verbose_name="Other domestic debt securities")
    IDSCOD = models.IntegerField(db_column="IDSCOD",verbose_name="Privately issued residential mortgage-backed securities")
    SCCMMB = models.IntegerField(db_column="SCCMMB",verbose_name="Commercial mortgage-backed securities - Total")
    scabs = models.IntegerField(db_column="scabs",verbose_name="Asset backed securities")
    SCSFP = models.IntegerField(db_column="SCSFP",verbose_name="Structured financial products - Total")
    SCODOT = models.IntegerField(db_column="SCODOT",verbose_name="Other domestic debt securities - All other")
    scford = models.IntegerField(db_column="scford",verbose_name="Foreign debt securities")
    IDsceq = models.IntegerField(db_column="IDsceq",verbose_name="Equity securities not held for trading")
    sceq = models.IntegerField(db_column="sceq",verbose_name="Equity securities")
    sceqfv = models.IntegerField(db_column="sceqfv",verbose_name="Equity securities readily determinable fair values")
    idahta = models.IntegerField(db_column="idahta",verbose_name="Assets held in trading accounts for TFR Reporters")
    scres = models.IntegerField(db_column="scres",verbose_name="General valuation allowances for securities for TFR Reporters")
    scpledge = models.IntegerField(db_column="scpledge",verbose_name="Pledged securities")
    scmtgbk = models.IntegerField(db_column="scmtgbk",verbose_name="Mortgage-backed securities")
    idscgtpc = models.IntegerField(db_column="idscgtpc",verbose_name="Certificates of participation in pools of residential mortgages")
    scgty = models.IntegerField(db_column="scgty",verbose_name="Issued or guaranteed by U.S.")
    scodpc = models.IntegerField(db_column="scodpc",verbose_name="Privately issued")
    idsccmo = models.IntegerField(db_column="idsccmo",verbose_name="Collaterized mortgage obligations")
    sccol = models.IntegerField(db_column="sccol",verbose_name="CMOs issued by government agencies or sponsored agencies")
    scodpi = models.IntegerField(db_column="scodpi",verbose_name="Privately issued")
    IDSCCMT = models.IntegerField(db_column="IDSCCMT",verbose_name="Commercial mortgage-backed securities")
    SCCMPT = models.IntegerField(db_column="SCCMPT",verbose_name="Commercial mortgage pass-through securities")
    SCCMOT = models.IntegerField(db_column="SCCMOT",verbose_name="Other commercial mortgage-backed securities")
    scha = models.IntegerField(db_column="scha",verbose_name="Held to maturity securities (book value)")
    scaf = models.IntegerField(db_column="scaf",verbose_name="Available-for-sale securities (fair market value)")
    scrdebt = models.IntegerField(db_column="scrdebt",verbose_name="Total debt securities")
    scsnhaa = models.IntegerField(db_column="scsnhaa",verbose_name="Amortized cost")
    scsnhaf = models.IntegerField(db_column="scsnhaf",verbose_name="Fair value")
    trade = models.IntegerField(db_column="trade",verbose_name="Trading account assets")
    idtrrval = models.IntegerField(db_column="idtrrval",verbose_name="Revaluation gains on off-balance sheet contracts")
    trlreval = models.IntegerField(db_column="trlreval",verbose_name="Revaluation losses on off-balance sheet contracts")