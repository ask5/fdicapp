from django.db import models

class Income_Expense(models.Model):

    class Meta:
        managed = False
        db_table = "financials_income_and_expense"
        verbose_name = "Income and Expense"
        verbose_name_plural = "Income and Expense"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    intinc = models.IntegerField(db_column="intinc",verbose_name="Total interest income")
    eintexp = models.IntegerField(db_column="eintexp",verbose_name="Total interest expense")
    nim = models.IntegerField(db_column="nim",verbose_name="Net interest income")
    elnatr = models.IntegerField(db_column="elnatr",verbose_name="Provision for loan and lease losses")
    nonii = models.IntegerField(db_column="nonii",verbose_name="Total noninterest income")
    ifiduc = models.IntegerField(db_column="ifiduc",verbose_name="Gross Fiduciary activities income")
    iserchg = models.IntegerField(db_column="iserchg",verbose_name="Service charges on deposit accounts")
    igltrad = models.IntegerField(db_column="igltrad",verbose_name="Trading account gains and fees")
    idothnii = models.IntegerField(db_column="idothnii",verbose_name="Additional Noninterest Income")
    nonix = models.IntegerField(db_column="nonix",verbose_name="Total noninterest expense")
    esal = models.IntegerField(db_column="esal",verbose_name="Salaries and employee benefits")
    epremagg = models.IntegerField(db_column="epremagg",verbose_name="Premises and equipment expense")
    IDEOTH = models.IntegerField(db_column="IDEOTH",verbose_name="Additional noninterest expense")
    idpretx = models.IntegerField(db_column="idpretx",verbose_name="Pre-tax net operating income")
    iglsec = models.IntegerField(db_column="iglsec",verbose_name="Securities gains (losses)")
    itax = models.IntegerField(db_column="itax",verbose_name="Applicable income taxes")
    ibefxtr = models.IntegerField(db_column="ibefxtr",verbose_name="Income before extraordinary items")
    extra = models.IntegerField(db_column="extra",verbose_name="Extraordinary gains, net")
    netinc = models.IntegerField(db_column="netinc",verbose_name="Net income")
    NETIMIN = models.IntegerField(db_column="NETIMIN",verbose_name="Minority interest net income")
    NETINBM = models.IntegerField(db_column="NETINBM",verbose_name="Net income of bank and minority interests.")
    ntlnls = models.IntegerField(db_column="ntlnls",verbose_name="Net charge-offs")
    eqcdiv = models.IntegerField(db_column="eqcdiv",verbose_name="Cash dividends")
    eqcstkrx = models.IntegerField(db_column="eqcstkrx",verbose_name="Sale, conversion, retirement of capital stock, net")
    noij = models.IntegerField(db_column="noij",verbose_name="Net operating income")