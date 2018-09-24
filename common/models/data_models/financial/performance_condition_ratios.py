from django.db import models

class Performance_Condition_Ratios(models.Model):

    class Meta:
        managed = False
        db_table = "financials_performance_and_condition_ratios"
        verbose_name = "Performance and Condition and Ratios"
        verbose_name_plural = "Performance and Condition and Ratios"

    id = models.AutoField(primary_key=True)
    cert = models.FloatField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    idntilr = models.FloatField(db_column="idntilr",verbose_name="% of unprofitable institutions")
    idntigr = models.FloatField(db_column="idntigr",verbose_name="% of insitutions with earnings gains")
    intincy = models.FloatField(db_column="intincy",verbose_name="Yield on earning assets")
    intexpy = models.FloatField(db_column="intexpy",verbose_name="Cost of funding earning assets")
    nimy = models.FloatField(db_column="nimy",verbose_name="Net interest margin")
    noniiay = models.FloatField(db_column="noniiay",verbose_name="Noninterest income to average assets")
    nonixay = models.FloatField(db_column="nonixay",verbose_name="Noninterest expense to average assets")
    ELNATRY = models.FloatField(db_column="ELNATRY",verbose_name="Loan and lease loss provision to assets")
    noijy = models.FloatField(db_column="noijy",verbose_name="Net operating income to assets")
    roa = models.FloatField(db_column="roa",verbose_name="Return on assets (ROA)")
    roaptx = models.FloatField(db_column="roaptx",verbose_name="Pretax return on assets")
    roe = models.FloatField(db_column="roe",verbose_name="Return on Equity (ROE)")
    roeinjr = models.FloatField(db_column="roeinjr",verbose_name="Retained earnings to average equity (ytd only)")
    ntlnlsr = models.FloatField(db_column="ntlnlsr",verbose_name="Net charge-offs to loans")
    elnantr = models.FloatField(db_column="elnantr",verbose_name="Credit loss provision to net charge-offs")
    iderncvr = models.FloatField(db_column="iderncvr",verbose_name="Earnings coverage of net charge-offs (x)")
    eeffr = models.FloatField(db_column="eeffr",verbose_name="Efficiency ratio")
    astempm = models.FloatField(db_column="astempm",verbose_name="Assets per employee ($millions)")
    iddivnir = models.FloatField(db_column="iddivnir",verbose_name="Cash dividends to net income (ytd only)*")
    ERNASTR = models.FloatField(db_column="ERNASTR",verbose_name="Earning assets to total assets ratio")
    lnatresr = models.FloatField(db_column="lnatresr",verbose_name="Loss allowance to loans")
    lnresncr = models.FloatField(db_column="lnresncr",verbose_name="Loan loss allowance to noncurrent loans")
    nperfv = models.FloatField(db_column="nperfv",verbose_name="Noncurrent assets plus other real estate owned to assets")
    nclnlsr = models.FloatField(db_column="nclnlsr",verbose_name="Noncurrent loans to loans")
    LNLSNTV = models.FloatField(db_column="LNLSNTV",verbose_name="Net loans and leases to total assets")
    lnlsdepr = models.FloatField(db_column="lnlsdepr",verbose_name="Net loans and leases to deposits")
    idlncorr = models.FloatField(db_column="idlncorr",verbose_name="Net loans and leases to core deposits")
    DEPDASTR = models.FloatField(db_column="DEPDASTR",verbose_name="Total domestic deposits to total assets")
    eqv = models.FloatField(db_column="eqv",verbose_name="Equity capital to assets")
    rbc1aaj = models.FloatField(db_column="rbc1aaj",verbose_name="Core capital (leverage) ratio")
    rbc1rwaj = models.FloatField(db_column="rbc1rwaj",verbose_name="Tier 1 risk-based capital ratio")
    rbcrwaj = models.FloatField(db_column="rbcrwaj",verbose_name="Total risk-based capital ratio")
    RBCT1CER = models.FloatField(db_column="RBCT1CER",verbose_name="Common equity tier 1 capital ratio")
    asset5 = models.BigIntegerField(db_column="asset5",verbose_name="Average total assets")
    ernast5 = models.BigIntegerField(db_column="ernast5",verbose_name="Average earning assets")
    eq5 = models.BigIntegerField(db_column="eq5",verbose_name="Average equity")
    LNLSGR5 = models.BigIntegerField(db_column="LNLSGR5",verbose_name="Average total loans")