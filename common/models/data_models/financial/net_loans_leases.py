from django.db import models


class Net_Loans_Leases(models.Model):

    class Meta:
        managed = False
        db_table = "financials_net_loans_leases"
        verbose_name = "Net Loans and Leases"
        verbose_name_plural = "Net Loans and Leases"

    id = models.AutoField(primary_key=True)
    cert = models.IntegerField(db_column="cert", verbose_name="Certificate #")
    report_date = models.DateTimeField(db_column="repdte", verbose_name="Report Date")

    lnlsnet= models.IntegerField(db_column="lnlsnet",verbose_name="Net loans and leases")
    lnatres= models.IntegerField(db_column="lnatres",verbose_name="Loan loss allowance")
    lnlsgr= models.IntegerField(db_column="lnlsgr",verbose_name="Total loans and leases")
    lncontra= models.IntegerField(db_column="lncontra",verbose_name="Unearned income")
    idlnls= models.IntegerField(db_column="idlnls",verbose_name="Loans and leases, gross")
    lnre= models.IntegerField(db_column="lnre",verbose_name="All real estate loans")
    lnredom= models.IntegerField(db_column="lnredom",verbose_name="Real estate loans in domestic offices")
    lnrecons= models.IntegerField(db_column="lnrecons",verbose_name="Construction and development loans")
    LNRECNFM= models.IntegerField(db_column="LNRECNFM",verbose_name="Residential 1-4 family construction")
    LNRECNOT= models.IntegerField(db_column="LNRECNOT",verbose_name="Other construction, all land development and other land")
    lnrenres= models.IntegerField(db_column="lnrenres",verbose_name="Secured by nonfarm nonresidential properties")
    LNRENROW= models.IntegerField(db_column="LNRENROW",verbose_name="Nonfarm nonresidential secured by owner-occupied properties")
    LNRENROT= models.IntegerField(db_column="LNRENROT",verbose_name="Commercial real estate other non-farm non-residential")
    lnremult= models.IntegerField(db_column="lnremult",verbose_name="Multifamily residential real estate")
    lnreres= models.IntegerField(db_column="lnreres",verbose_name="1-4 family residential loans")
    lnreag= models.IntegerField(db_column="lnreag",verbose_name="Farmland loans")
    lnrefor= models.IntegerField(db_column="lnrefor",verbose_name="Loans held in foreign offices")
    lnag= models.IntegerField(db_column="lnag",verbose_name="Farm loans")
    lnci= models.IntegerField(db_column="lnci",verbose_name="Commercial and industrial loans")
    lncinus= models.IntegerField(db_column="lncinus",verbose_name="To non-U.S. addressees")
    lncon= models.IntegerField(db_column="lncon",verbose_name="Loans to individuals")
    lncrcd= models.IntegerField(db_column="lncrcd",verbose_name="Credit card loans")
    lnconrp= models.IntegerField(db_column="lnconrp",verbose_name="Related Plans")
    LNAUTO= models.IntegerField(db_column="LNAUTO",verbose_name="Consumer Loans - Auto")
    lnconoth= models.IntegerField(db_column="lnconoth",verbose_name="Other loans to individuals")
    lnotci= models.IntegerField(db_column="lnotci",verbose_name="All other loans & leases")
    lnfg= models.IntegerField(db_column="lnfg",verbose_name="Loans to foreign governments and official institutions")
    lnmuni= models.IntegerField(db_column="lnmuni",verbose_name="Obligations of states and political subdivisions in U.S.")
    idothlns= models.IntegerField(db_column="idothlns",verbose_name="Other loans")
    ls= models.IntegerField(db_column="ls",verbose_name="Lease financing receivables")
    lndepac= models.IntegerField(db_column="lndepac",verbose_name="Loans to depository institutions and acceptances of other banks")
    lncomre= models.IntegerField(db_column="lncomre",verbose_name="Loans not secured by real estate")
    lnrenus= models.IntegerField(db_column="lnrenus",verbose_name="Loans secured by real estate to non-U.S. addressees")
    rslnltot= models.IntegerField(db_column="rslnltot",verbose_name="Restructured Loans & leases")
    rslnls= models.IntegerField(db_column="rslnls",verbose_name="Non 1-4 family restructured loans & leases")
    RB2LNRES= models.IntegerField(db_column="RB2LNRES",verbose_name="Allowance for loan and lease losses in tier 2")
    lnlsgrf= models.IntegerField(db_column="lnlsgrf",verbose_name="Total loans and leases")