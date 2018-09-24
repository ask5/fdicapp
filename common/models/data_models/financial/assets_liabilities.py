from django.db import models


class Assets_Liabilities(models.Model):

    class Meta:
        managed = False
        db_table = "financials_assets_and_liabilities"
        verbose_name = "Assets and Liabilities"
        verbose_name_plural = "Assets and Liabilities"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    numemp = models.IntegerField(db_column="numemp",
                               verbose_name="Total employees",
                               help_text="Total employees (full-time equivalent)")

    asset = models.BigIntegerField(db_column="asset",verbose_name="Total assets")

    chbal = models.BigIntegerField(db_column="asset", verbose_name="Cash & Balances",
                                   help_text="Cash & Balances due from depository institutions")

    chbali = models.BigIntegerField(db_column="chbali", help_text="Interest-bearing balances")
    sc = models.BigIntegerField(db_column="sc", help_text="Total securities")
    frepo = models.BigIntegerField(db_column="frepo", help_text="Federal funds sold and reverse repurchase")
    lnlsnet = models.BigIntegerField(db_column="lnlsnet", help_text="Net loans and leases")
    lnatres = models.BigIntegerField(db_column="lnatres", help_text="Loan loss allowance")
    trade = models.BigIntegerField(db_column="trade", help_text="Trading account assets")
    bkprem = models.BigIntegerField(db_column="bkprem", help_text="Bank premises and fixed assets")
    ore = models.BigIntegerField(db_column="ore", help_text="Other real estate owned")
    intan = models.BigIntegerField(db_column="intan", help_text="Goodwill and other intangibles")
    idoa = models.BigIntegerField(db_column="idoa", help_text="All other assets")
    liabeq = models.BigIntegerField(db_column="liabeq", help_text="Total liabilities and capital")
    liab = models.BigIntegerField(db_column="liab", help_text="Total Liabilities")
    dep = models.BigIntegerField(db_column="dep", help_text="Total deposits")
    depi = models.BigIntegerField(db_column="depi", help_text="Interest-bearing deposits")
    depdom = models.BigIntegerField(db_column="depdom", help_text="Deposits held in domestic offices")
    iddepinr = models.BigIntegerField(db_column="iddepinr", help_text="% insured (estimated)")
    frepp = models.BigIntegerField(db_column="frepp", help_text="Federal funds purchased and repurchase agreements")
    tradel = models.BigIntegerField(db_column="tradel", help_text="Trading liabilities")
    idobrmtg = models.BigIntegerField(db_column="idobrmtg", help_text="Other borrowed funds")
    subnd = models.BigIntegerField(db_column="subnd", help_text="Subordinated debt")
    idoliab = models.BigIntegerField(db_column="idoliab", help_text="All other liabilities")
    eqtot = models.BigIntegerField(db_column="eqtot", help_text="Total equity capital")
    eq = models.BigIntegerField(db_column="eq", help_text="Bank equity capital")
    eqpp = models.BigIntegerField(db_column="eqpp", help_text="Perpetual preferred stock")
    eqcs = models.BigIntegerField(db_column="eqcs", help_text="Common stock")
    eqsur = models.BigIntegerField(db_column="eqsur", help_text="Surplus")
    equptot = models.BigIntegerField(db_column="equptot", help_text="Undivided profits")
    eqconsub = models.BigIntegerField(db_column="eqconsub", help_text="Equity, minor interest in consolidated subs")
    nclnls = models.BigIntegerField(db_column="nclnls", help_text="Noncurrent loans and leases")
    ncgtypar = models.BigIntegerField(db_column="ncgtypar", help_text="Noncurrent loans which are wholly or partially guaranteed by the U.S.")
    oaienc = models.BigIntegerField(db_column="oaienc", help_text="Income earned, not collected on loans")
    ernast = models.BigIntegerField(db_column="ernast", help_text="Earning assets")
    asstlt = models.BigIntegerField(db_column="asstlt", help_text="Long-term assets (5+ years)")
    asset5 = models.BigIntegerField(db_column="Asset5", help_text="Average total assets")
    asset2 = models.BigIntegerField(db_column="asset2", help_text="Average assets, quarterly")
    rwajt = models.BigIntegerField(db_column="RWAJT", help_text="Total risk weighted assets adjusted")
    avassetj = models.BigIntegerField(db_column="avassetj", help_text="Adjusted average assets for leverage capital purposes")
    oalifins = models.BigIntegerField(db_column="OALIFINS", help_text="Life insurance assets")
    oalifgen = models.BigIntegerField(db_column="OALIFGEN", help_text="General account life insurance assets")
    oalifsep = models.BigIntegerField(db_column="OALIFSEP", help_text="Separate account life insurance assets")
    oalifhyb = models.BigIntegerField(db_column="Oalifhyb", help_text="Hybrid life insurance assets")
    voliab = models.BigIntegerField(db_column="voliab", help_text="Volatile liabilities")
    lnexamt = models.BigIntegerField(db_column="lnexamt", help_text="Insider loans")
    othbfhlb = models.BigIntegerField(db_column="othbfhlb", help_text="FHLB advances")
    lnlssale = models.BigIntegerField(db_column="lnlssale", help_text="Loans and leases held for sale")
    ucln = models.BigIntegerField(db_column="ucln", help_text="Unused loan commitments")
    rbct1j = models.BigIntegerField(db_column="rbct1j", help_text="Tier one (core) capital")
    rbct2 = models.BigIntegerField(db_column="rbct2", help_text="Tier 2 Risk-based capital")
    uc = models.BigIntegerField(db_column="uc", help_text="Total unused commitments")
    obsdir = models.BigIntegerField(db_column="obsdir", help_text="Derivatives")