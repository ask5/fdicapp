from django.db import models
from .region import *
from .regulatory import *
from .misc import *


class Institution(models.Model):
    cert = models.IntegerField(primary_key=True,
                               db_column="CERT",
                               verbose_name="FDIC Certificate #",
                               help_text="A unique NUMBER assigned by the FDIC used to identify institutions and for "
                                         "the issuance of insurance certificates.")
    state_name = models.CharField(db_column="STNAME",
                                  max_length=50,
                                  verbose_name="State Name",
                                  help_text="State in which the institution is physically located. "
                                            "The FDIC Act defines state as any State of the United States, "
                                            "the District of Columbia, and any territory of the United States, "
                                            "Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific "
                                            "Islands, the Virgin Island, and the Northern Mariana Islands.",
                                  )
    docket = models.IntegerField(db_column="DOCKET",
                                 verbose_name="OTS Docket Number",
                                 help_text="An identification number assigned to institutions chartered by the office "
                                           "of thrift supervision or members of the federal housing finance board (FHFB)"
                                           " and formerly by the federal home loan bank board.  The value is '00000' "
                                           "for institutions not members of the FHFB.")
    active = models.BooleanField(db_column="ACTIVE",
                                 verbose_name="Active Status",
                                 help_text="Institutions that are currently open and insured by the FDIC.")
    address = models.CharField(db_column="ADDRESS",
                               max_length=255,
                               verbose_name="Physical Street Address",
                               help_text="Street address at which the institution or one of its branches is "
                                         "physically located.")
    asset = models.BigIntegerField(db_column="ASSET",
                                   verbose_name="Total assets",
                                   help_text="The sum of all assets owned by the institution including cash, loans, "
                                             "securities, bank premises and other assets. "
                                             "This total does not include off-balance-sheet accounts.")
    bk_class = models.ForeignKey(Charter_Class,
                                db_column="BKCLASS",
                                on_delete=models.DO_NOTHING,
                                verbose_name="Bank Charter Class",
                                help_text="A classification code assigned by the FDIC based on the institution's "
                                          "charter type (commercial bank or savings institution), charter agent "
                                          "(state or federal), Federal Reserve membership status "
                                          "(Fed member, Fed nonmember)and its primary federal regulator "
                                          "(state chartered institutions are subject to both federal and state "
                                          "supervision). N = commercial bank, national (federal) charter and Fed member"
                                          ", supervised by the Office of the Comptroller of the Currency (OCC)."
                                          "SM = commercial bank, state charter and Fed member, supervised by the "
                                          "Federal Reserve (FRB). NM = commercial bank, state charter and "
                                          "Fed nonmember, supervised by the FDIC  SB = savings banks, state charter, "
                                          "supervised by the FDIC. SA = savings associations, state or federal charter,"
                                          "supervised by the Office of Thrift Supervision (OTS). "
                                          "OI = insured U.S. branch of a foreign chartered institution (IBA).")

    change_code_1 = models.ForeignKey(Structure_Code,
                                      on_delete=models.DO_NOTHING,
                                      related_name="change_code_1",
                                      related_query_name="change_code_1",
                                      db_column="CHANGEC1",
                                      verbose_name="Change Code 1",
                                      help_text="FDIC code used to signify a structural event relating to an institution.")
    change_code_2 = models.ForeignKey(Structure_Code,
                                      on_delete=models.DO_NOTHING,
                                      db_column="CHANGEC2",
                                      related_name="change_code_2",
                                      related_query_name="change_code_2",
                                      verbose_name="Change Code 2",
                                      help_text="FDIC code used to signify a structural event relating to an institution.")
    change_code_3 = models.ForeignKey(Structure_Code,
                                      on_delete=models.DO_NOTHING,
                                      db_column="CHANGEC3",
                                      verbose_name="Change Code 3",
                                      related_name="change_code_3",
                                      related_query_name="change_code_3",
                                      help_text="FDIC code used to signify a structural event relating to an institution.")
    change_code_4 = models.ForeignKey(Structure_Code,
                                      on_delete=models.DO_NOTHING,
                                      db_column="CHANGEC4",
                                      verbose_name="Change Code 4",
                                      related_name="change_code_4",
                                      related_query_name="change_code_4",
                                      help_text="FDIC code used to signify a structural event relating to an institution.")
    change_code_5 = models.ForeignKey(Structure_Code,
                                      on_delete=models.DO_NOTHING,
                                      db_column="CHANGEC5",
                                      verbose_name="Change Code 5",
                                      related_name="change_code_5",
                                      related_query_name="change_code_5",
                                      help_text="FDIC code used to signify a structural event relating to an institution.")

    charter = models.IntegerField(db_column="CHARTER",
                                  verbose_name="OCC Charter Number",
                                  help_text="A unique number assigned by the Office of the Comptroller of the Currency "
                                            "(OCC) used to identify institutions that it has chartered and regulates "
                                            "(i.e. national  banks).")
    charting_agency = models.ForeignKey(Charting_Agency,
                                       db_column="CHRTAGNT",
                                       on_delete=models.DO_NOTHING,
                                       verbose_name="Chartering Agency",
                                       help_text="All Chartering Agencies - State and Federal  Comptroller of the "
                                                 "Currency - Chartering authority for nationally chartered commercial "
                                                 "banks and for federally chartered savings associations (The Office of"
                                                 " Thrift Supervision (OTS) before 7/21/11)  State "
                                                 "(includes U.S. Territories) - Chartering authority for institutions "
                                                 "that are not chartered by the OCC or OTS")

    conservatorship = models.CharField(db_column="CONSERVE",
                                       max_length=1,
                                       verbose_name="conservatorship",
                                       help_text="A flag (1=yes;0=no) that indicates if an institution is being "
                                                 "operated in government conservatorship.")

    city = models.CharField(db_column="CITY",
                            max_length=50,
                            verbose_name="City",
                            help_text="City in which an institution's headquarters or one of its branches is "
                                      "physically located. Either the entire name or part of the name of a specific "
                                      "city may be entered to produce an Institution List.")

    cl_code = models.IntegerField(db_column="CLCODE",
                                  verbose_name="Numeric Code",
                                  help_text="Numeric code which identifies the major and minor categories of an "
                                            "institution. ")

    cmsa_number = models.IntegerField(db_column="CMSA_NO",
                               verbose_name="Consolidated Metropolitan Statistical Division Number",
                               help_text="The numeric code given by the US Census Bureau office of Management and Budget that represents the CMSA prior to the year 2000 standards. 1=yes")


    cmsa = models.CharField(db_column="CMSA",
                                max_length=300,
                                verbose_name="Consolidated Metropolitan Statistical Area",
                                help_text="The Federal Information Processing Standards (FIPS) Consolidated Metropolitan"
                                          " Statistical Area (CMSA) code is a number "
                                          "representing the institution location. A CMSA consists of two or more "
                                          "contiguous Metropolitan Statistical Areas (MSA) "
                                          "with a combined population of over 1 Million.  "
                                          "Note: If an institution is not located in a CMSA, the value of the field will"
                                          " be zeroes. ")

    county = models.CharField(db_column="COUNTY",
                                max_length=50,
                                verbose_name="County",
                                help_text="County where the institution is physically located (abbreviated if the county name exceeds 16 characters).")

    last_updated_date = models.DateTimeField(db_column="DATEUPDT",
                                             verbose_name="Last Updated Date",
                                             help_text="The date of the last data update")

    denovo = models.IntegerField(db_column="DENOVO",
                                 verbose_name="Denovo Institution",
                                 help_text="A flag used to indicate whether an institution is a new institution "
                                           "(not a recharter). This flag is set quarterly. For instance, "
                                           "if REPDTE is 3/31/98 and DENOVO equals 1, the institution was a denovo "
                                           "during the first quarter of 1998.")
    total_deposits = models.BigIntegerField(db_column="DEP",
                                            verbose_name="Total Deposits",
                                            help_text="The sum of all deposits including demand deposits, money market "
                                                      "deposits, other savings deposits, time deposits and deposits in "
                                                      "foreign offices.")

    effective_date = models.DateTimeField(db_column="EFFDATE",
                                          verbose_name="Last Structure Change Effective Date",
                                          help_text="Effective Start Date of the data contained in this row.")

    end_date = models.DateTimeField(db_column="ENDEFYMD",
                                    verbose_name="End Date",
                                    help_text="The date that ends or closes out the last structural event relating "
                                              "to an institution. For closed institutions, this date represents "
                                              "the day that the institution became inactive.")
    equity_capital = models.BigIntegerField(db_column="EQ",
                                            verbose_name="Equity capital",
                                            help_text="Total equity capital (includes preferred and common stock, "
                                                      "surplus and undivided profits).")
    established_date = models.DateTimeField(db_column="ESTYMD",
                                            verbose_name="Established Date",
                                            help_text="The date on which the institution began operations.")

    fdic_geographic_region = models.ForeignKey(FDIC_Region,
                                               on_delete=models.DO_NOTHING,
                                               db_column="FDICDBS",
                                               verbose_name="Geographic Region",
                                               help_text="The FDIC Office assigned to the geographic area.  The eight FDIC Regions and their respective states are:    Boston - Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont  New York - Delaware, District of Columbia, Maryland, New Jersey, New York, Pennsylvania, Puerto Rico, U.S. Virgin Islands  Atlanta - Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia, West Virginia  Memphis - Arkansas, Kentucky, Louisiana, Mississippi, Tennessee  Chicago - Illinois, Indiana, Michigan, Ohio, Wisconsin   Kansas City - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota  Dallas - Colorado, New Mexico, Oklahoma, Texas  San Francisco - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, Oregon, States of Micronesia, Utah, Washington, Wyoming ")

    fed = models.ForeignKey(Federal_Reserve_District,
                            on_delete=models.DO_NOTHING,
                            db_column="FED",
                            verbose_name="Federal Reserve District",
                            help_text="A number used to identify the Federal Reserve district in which the institution is located.")

    federal_charter = models.BooleanField(db_column="FEDCHRTR",
                                          verbose_name="Federal Charter",
                                          help_text="A flag used to indicate whether the institution is chartered by an agent of the federal government.")

    federal_reserve_id = models.IntegerField(db_column="FED_RSSD",
                                             verbose_name="Federal Reserve ID Number",
                                             help_text="A unique number assigned by the Federal Reserve board as the entity's unique identifier")
    fdic_field_office = models.CharField(db_column="FLDOFF",
                                         max_length=50,
                                         verbose_name="Field Office",
                                         help_text="The FDIC Field Office where an institution is physically located.")

    iba = models.BooleanField(db_column="IBA",
                              verbose_name="Insured offices of foreign banks",
                              help_text="Includes Bank Insurance Fund insured branches in the U.S. established by banks chartered and headquartered in foreign countries.  These institutions are regulated by one of the three Federal commercial bank regulators and submit financial data to the Federal Reserve.")

    inactive = models.BooleanField(db_column="INACTIVE",
                                   verbose_name="Inactive",
                                   help_text="Institutions that are currently closed but were once insured by the FDIC.")

    insurance_fund_membership = models.CharField(db_column="INSAGNT1",
                                                 max_length=5,
                                                 verbose_name="Insurance Fund Membership",
                                                 help_text="Deposit Insurance Fund (DIF), Bank Insurance Fund (BIF), Savings Association Insurance Fund (SAIF)")

    secondary_insurance_fund = models.CharField(db_column="INSAGNT2",
                                                max_length=5,
                                                verbose_name="Secondary Insurance Fund",
                                                help_text="As a result of the establishment of a single Deposit Insurance Fund (DIF) effective April 1, 2006, the Secondary Insurance fund is no longer applicable. previously both bif and saif bank insurance fund - institutions that are members of the bank insurance fund savings association insurance fund - Institutions that are members of the Savings Association Insurance Fund")

    deposit_insurance_date = models.DateTimeField(db_column="INSDATE",
                                                  verbose_name="Date of Deposit Insurance",
                                                  help_text="The date that an institution obtained federal deposit insurance.")

    credit_card_institutions = models.BooleanField(db_column="INSTCRCD",
                                                   verbose_name="Credit Card Institutions",
                                                   help_text="Institutions with total loans greater than 50% of total assets and credit card loans greater than 50% of total loans, including loans that have been securitized and sold.")

    bank_insurance_fund = models.BooleanField(db_column="INSBIF",
                                              verbose_name="Credit Card Institutions",
                                              help_text="Institutions who are members of the Bank Insurance Fund. As of April 1, 2006 BIF was merged together with the Savings Institution Insurance Fund (SAIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured BIF member institutions, that are still active or open, are now insured members of DIF.")

    insured_commercial_banks = models.BooleanField(db_column="INSCOML",
                                                   verbose_name="Insured commercial banks",
                                                   help_text="Includes commercial banks insured by the FDIC.  These institutions are regulated by one of the three Federal commercial bank regulators (FDIC, Federal Reserve Board, or Office of the Comptroller of the Currency).  They submit financial reports to the Federal Reserve (state member banks) or the FDIC (state non-member banks and national banks).")

    fdic_insured = models.BooleanField(db_column="INSFDIC",
                                       verbose_name="FDIC Insured",
                                       help_text="Includes institutions insured by the FDIC.")

    saif_insured = models.BooleanField(db_column="INSSAIF",
                                       verbose_name="SAIF Insured",
                                       help_text="Institutions who are members of the Savings Association Insurance Fund. As of April 1, 2006 SAIF was merged together with the Bank Insurance Fund (BIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured SAIF member institutions, that are still active or open, are now insured members of DIF.")

    insured_savings = models.BooleanField(db_column="INSSAVE",
                                          verbose_name="Insured Savings Institution",
                                          help_text="Includes savings institutions insured by the FDIC that operate under state or federal banking codes applicable to thrift institutions.  These institutions are regulated by and submit financial reports to one of two Federal regulators (FDIC or Office of Thrift Supervision).")

    name = models.CharField(db_column="NAME",
                            max_length=255,
                            verbose_name="Institution name",
                            help_text="The legal name of the institution.")

    new_cert = models.IntegerField(db_column="NEWCERT",
                                   verbose_name="New certificate number",
                                   help_text="A new certificate number of an already existing FDIC-insured institution resulting from either a merger or an acquisition.")

    oakar = models.BooleanField(db_column="OAKAR",
                                verbose_name="Oakar Institutions",
                                help_text="A member of one insurance fund that acquired deposits insured by the other fund, where that portion of the buyer's deposits remained insured by, and assessable by, the other fund.")

    occ_district = models.ForeignKey(OCC_District,
                                     on_delete=models.DO_NOTHING,
                                     db_column="OCCDIST",
                                     verbose_name="Office of the Comptroller",
                                     help_text="The Office of the Comptroller of the Currency (OCC) District in which the institution is physically located. The six OCC Districts and their respective states are: Northeast - Connecticut, Delaware, District of Columbia, Maine, Maryland, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Puerto Rico, Rhode Island, Vermont, U.S. Virgin Islands  Southeast - Alabama, Florida, Georgia, Mississippi, North Carolina, South Carolina, Tennessee, Virginia, West Virginia  Central - Illinois, Indiana, Kentucky, Michigan, Ohio, Wisconsin  Midwest - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota  Southwest - Arkansas, Louisiana, New Mexico, Oklahoma, Texas  West - Alaska, American Samoa, Arizona, California, Colorado, Guam, Hawaii, Idaho, Montana, Nevada, Oregon, States of Micronesia, Utah, Washington, Wyoming")

    ots_district = models.IntegerField(db_column="OTSDIST",
                                       verbose_name="OTS District",
                                       help_text="Office of Thrift Supervision (OTS) District - Sunset (ended)  7/21/11")

    process_date = models.DateTimeField(db_column="PROCDATE",
                                        verbose_name="Last Structure Change Process Date",
                                        help_text="A date field indicating the date that a change to this record was processed. Standard format = 'CCYYMMDD' (Length = 8) "
                                                  "which has been converted to Month, Day, Year format for display purposes.")

    qbp_region = models.ForeignKey(QBP_Region,
                                   on_delete=models.DO_NOTHING,
                                   db_column="QBPRCOML",
                                   verbose_name="Quarterly Banking Profile Commercial Bank Region",
                                   help_text="The Quarterly Banking Profile (QBP) Commercial Bank Region in which the institution is physically located. "
                                             "Select from a drop down box. "
                                             "regional breakdown"
                                             " group data by qbp region is only available for insured commercial banks "
                                             "and insured savings institutions and NOT All Insured Institutions, "
                                             "Insured Commercial Banks by asset size and Insured Savings Institutions by asset size.")

    report_date = models.DateTimeField(db_column="REPDTE",
                                       verbose_name="Report Date",
                                       help_text="The last day of the financial reporting period selected.")

    ris_date = models.DateTimeField(db_column="RISDATE",
                                    verbose_name="RIS Date",
                                    help_text="The financial reporting period selected in CCYYMM format.")

    state_charter = models.BooleanField(db_column="STCHRTR",
                                        verbose_name="State Charter",
                                        help_text="A flag (1=yes;0=no) that indicates if an institution is state chartered.")

    roa = models.FloatField(db_column="ROA",
                            verbose_name="Return on Assets (ROA)",
                            help_text="Net income after taxes and extraordinary items (annualized) as a percent of average total assets.")

    quarterly_roa = models.FloatField(db_column="ROAQ",
                                      verbose_name="Quarterly Return on Assets",
                                      help_text="Quarterly net income after taxes and extraordinary items as a percent of average total assets.")

    roe = models.FloatField(db_column="ROE",
                            verbose_name="Return on Equity (ROE)",
                            help_text="Annualized net income as a percent of average equity on a consolidated basis.     Note: If retained earnings are  negative, the ratio is shown as NA.")

    quarterly_roe = models.FloatField(db_column="ROEQ",
                                      verbose_name="Quarterly return on equity",
                                      help_text="Quarterly net income (including gains or losses on securities and extraordinary items) as a percentage of average total equity capital.")

    run_date = models.DateTimeField(db_column="RUNDATE",
                                    verbose_name="Run Date",
                                    help_text="The day the institution information was updated.")

    sasser = models.BooleanField(db_column="SASSER",
                                 verbose_name="Sasser Institutions",
                                 help_text="OTS supervised savings associations that converted their charter to that of a commercial or savings bank.  Converted associations remain members of the SAIF, but they become subject to supervision by one of the three federal banking agencies. Not Applicable as of March 31, 2006.")

    state_alpha_code = models.CharField(db_column="STALP",
                                        max_length=2,
                                        verbose_name="State Alpha code",
                                        help_text="State in which the the headquarters are physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.")

    state_county_num = models.CharField(db_column="STCNTY",
                                        max_length=10,
                                        verbose_name="State and county number",
                                        help_text="A five digit number representing the state and county in which the institution is physically located.  The first two digits represent the FIPS state numeric code and the last three digits represent the FIPS county numeric code.")

    web_address = models.CharField(db_column="WEBADDR",
                                   max_length=500,
                                   verbose_name="Primary Internet Web Address",
                                   help_text="The primary internet site address is the public internet site obtained from the most recent FFIEC Call Report (CALL) for commercial banks or from the supplemental information for Thrift Financial Reporters (TFR). The primary internet site address is included only for those institutions reporting an address on the most recent FFIEC Call Report or Thrift Financial Report.  This information resides in the most recent demographic information file. For some institutions users will find that for the item Primary Internet Web Address: the caption will read 'Web site not available'.  Possible reasons that a Web site may not be available are: The institution failed to file on the most recent call report or TFR. The institution filed a primary Internet Web address on its most recent FFIEC Call Report; however, the address filed by the institution was not in accordance with the instructions provided by the FFIEC on how to file a primary Internet Web address or FDIC attempts to validate and access the site were unsuccessful. Users may also experience instances where the URL provided for primary Internet Web address in ID returns an error stating that the site is not found. Possible reasons for such occurrences are: The institution?s reported primary Web address was valid as of the date that the demographic information was updated in ID, but is no longer valid. The institution?s reported Internet Web address is valid, but the institution?s Web site was inoperable at the time that the user attempted to access it due to technical problems being experienced by the institution?s Web site, the institution?s site provider, the user?s Web provider, or other issues not related to the validity of the Web address.  Users are advised to contact the institution on any questions regarding the services provided by the institution. For questions involving the reporting of primary Internet Web address by those institutions that file a FFIEC Call report, users are advised to contact supervision@fdic.gov.  For questions involving the primary Internet Web address of institutions that file a Thrift Financial Report, users are advised to contact pamela.schaar@ots.treas.gov or call Ms. Schaar at (202) 906-7205. Disclaimer: The Primary Internet Web Addresses listed have been reported to the FDIC by each institution. The hyperlinks to institution Internet sites are provided solely as a convenience to users of the FDIC Internet site. The FDIC has made a limited effort to determine that these links function properly. However, linked sites are not under the control of FDIC, and FDIC is not responsible for the contents of any linked site, or any link contained in a linked site.  Even if you access an institution?s site by means of the link provided by FDIC, you are responsible for confirming the identity and authenticity of any institution you visit and transact business with online. The inclusion of a link does not imply or constitute an endorsement by FDIC of the institution, its ownership or management, the products or services it offers, or any advertisers or sponsors appearing on the institution?s site site.")

    zip_code = models.CharField(db_column="ZIP",
                                max_length=10,
                                verbose_name="Zip Code",
                                help_text="The first three, four, or five digits of the full postal zip code representing physical location of the institution or its branch office.")

    multibank_holding = models.BooleanField(db_column="HCTMULT",
                                            verbose_name="Bank Holding Company Type",
                                            help_text="A flag used to indicate whether an institution is a member of a multibank holding company 1=yes, 0=no")

    regulator = models.ForeignKey(Regulator,
                                   on_delete=models.DO_NOTHING,
                                   db_column="REGAGNT",
                                   verbose_name="Regulator",
                                   help_text="There are four Federal regulators of banks and savings and loan institutions: federal deposit insurance corporation (fdic) - primary federal regulator responsible for state-chartered banks not members of the Federal Reserve System and state chartered savings banks. Federal Reserve Board (FRB) - Primary Federal regulator responsible for state-chartered commercial bank members of the Federal Reserve System. Office of the Comptroller of the Currency (OCC) - Primary Federal regulator responsible for nationally chartered commercial banks and federally chartered savings and loan associations. Before 7/21/11, Office of Thrift Supervision (OTS) - Primary Federal regulator responsible for federally chartered savings and loan associations, federal savings banks and state-chartered savings and loan associations. FDIC insured depository institutions are members of the Deposit Insurance Fund (DIF).")


    msa = models.CharField(db_column="MSA",
                                max_length=300,
                                verbose_name="Metropolitan Statistical Area (MSA)",
                                help_text="The Metropolitan Statistical Areas based on Census Bureau data, "
                                          "as defined by the US Office of Management (OMB) prior to the year 2000.")


    ots_supervision_region = models.ForeignKey(OTS_Region,
                                   on_delete=models.DO_NOTHING,
                                   db_column="OTSREGNM",
                                   verbose_name="Office of Thrift Supervision Region",
                                   help_text="Prior to 7/21/11, the Office of Thrift Supervision (OTS) Region in which the institution is physically located. The five OTS Regions and their respective states are: Northeast - Connecticut, Delaware, Maine, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, West Virginia Southeast - Alabama, District of Columbia, Florida, Georgia, Maryland, North Carolina, Puerto Rico, South Carolina, U.S. Virgin Islands, Virginia Central - Illinois, Indiana, Kentucky, Michigan, Ohio, Tennessee, Wisconsin Midwest - Arkansas, Colorado, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Nebraska, New Mexico, North Dakota, Oklahoma, South Dakota, Texas West - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, States of Micronesia, Oregon, Utah, Washington, Wyoming ")

    supervisory_region = models.ForeignKey(Supervisory_Region,
                                   on_delete=models.DO_NOTHING,
                                   db_column="FDICREGN",
                                   verbose_name="FDIC Supervisory Region",
                                   help_text="The supervisory FDIC office assigned to the institution.  The eight FDIC Supervisory Regions and their respective states are:    Boston - Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont  New York - Delaware, District of Columbia, Maryland, New Jersey, New York, Pennsylvania, Puerto Rico, U.S. Virgin Islands  Atlanta - Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia, West Virginia  Memphis - Arkansas, Kentucky, Louisiana, Mississippi, Tennessee  Chicago - Illinois, Indiana, Michigan, Ohio, Wisconsin   Kansas City - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota  Dallas - Colorado, New Mexico, Oklahoma, Texas  San Francisco - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, Oregon, States of Micronesia, Utah, Washington, Wyoming")

    offices = models.IntegerField(db_column="OFFICES",
                                       verbose_name="Offices",
                                       help_text="A branch/office is any location, or facility, of a financial "
                                                 "institution, including its main office, where deposit accounts are "
                                                 "opened, deposits are accepted, checks paid, and loans granted. "
                                                 "Some branches include, but are not limited to, brick and mortar "
                                                 "locations, detached or attached drive-in facilities, seasonal offices,"
                                                 " offices on military bases or government installations, "
                                                 "paying/receiving stations or units, nondeposit offices, Internet and "
                                                 "PhoneBanking locations where a customer can open accounts, make "
                                                 "deposits and borrow money. A branch does not include Automated "
                                                 "Teller Machines (ATM), Consumer Credit Offices, Contractual Offices, "
                                                 "Customer Bank Communication Terminals (CBCT), Electronic Fund Transfer"
                                                 " Units (EFTU), and Loan Production Offices Summary of Deposits "
                                                 "information is required for each insured office located in any State, "
                                                 "the District of Columbia, the Commonwealth of Puerto Rico or any U.S. "
                                                 "territory or possession such as Guam or the U.S. Virgin Islands, "
                                                 "without regard to the location of the main office.")

    city_of_high_holder = models.CharField(db_column="CITYHCR",
                                   max_length=50,
                                   verbose_name="City of High Holder",
                                   help_text="City in which the headquarters of the institution's regulatory high holder"
                                             " are physically located.")

    domestic_deposits = models.BigIntegerField(db_column="DEPDOM",
                                            verbose_name="Deposits held in domestic offices",
                                            help_text="The sum of all domestic office deposits, including demand "
                                                      "deposits, money market deposits, other savings deposits "
                                                      "and time deposits.")

    form_31 = models.BooleanField(db_column="FORM31",
                                       verbose_name="FFIEC Call Report 31 Filer",
                                       help_text="A flag (1=yes,0=no) that indicates whether and institution filed an "
                                                 "FFIEC 031 Call Report.  "
                                                 "Commercial banks with domestic and foreign offices are required to "
                                                 "file such a report.")

    agri_lending_institution = models.BooleanField(db_column="INSTAG",
                                       verbose_name="Agricultural lending institution indicator",
                                       help_text="An indicator specifying whether an institution is primarily an "
                                                 "agricultural lending institution.")

    ownership_type = models.BooleanField(db_column="MUTUAL",
                                       verbose_name="Ownership Type",
                                       help_text="Banking institutions fall into one of two ownership types, stock or "
                                                 "non-stock. An institution which sells stock to raise capital is "
                                                 "called a stock institution. It is owned by the shareholders who "
                                                 "benefit from profits earned by the institution. A non-stock "
                                                 "institution, or mutual institution, is owned and controlled solely by "
                                                 "its depositors. A mutual does not issue capital stock.")

    holding_company = models.CharField(db_column="NAMEHCR",
                            max_length=255,
                            verbose_name="Bank Holding Company (Regulatory Top Holder)",
                            help_text="Note: Information on bank holding companies is only as of quarter-end.Regulatory "
                                      "top holder is any company that    directly or indirectly owns, controls or "
                                      "has power to vote 25 percent or more of a bank's or direct holding company's "
                                      "shares or  controls in any manner the election of a majority of the directors or "
                                      "trustees of a bank or direct holding company or  exercises a controlling "
                                      "influence over the management or policies of a bank or direct holding company.   "
                                      "Information on Thrift Holding Companies that own Savings Associations but do not "
                                      "own banks is not currently available in the ID System.  Source:  Federal Reserve "
                                      "Board National Information Center data base.")

    net_income = models.BigIntegerField(db_column="NETINC",
                                            verbose_name="Net Income",
                                            help_text="Net interest income plus total noninterest income plus realized "
                                                      "gains (losses) on securities and extraordinary items, less total "
                                                      "noninterest expense, loan loss provisions and income taxes.")

    net_income_quarterly = models.BigIntegerField(db_column="NETINCQ",
                                            verbose_name="Net Income Quarterly",
                                            help_text="Quarterly net interest income plus total noninterest income plus realized gains (losses) on securities and extraordinary items, less total noninterest expense, loan loss provisions and income taxes.")

    domestic_offices = models.IntegerField(db_column="OFFDOM",
                                       verbose_name="Number of Domestic Offices",
                                       help_text="The number of domestic offices (including headquarters) operated by active institutions in the U.S., territories and possessions.")

    foreign_offices = models.IntegerField(db_column="OFFFOR",
                                       verbose_name="Number of Foreign Offices",
                                       help_text="The number of foreign offices (outside the U.S.) operated by the institution.")

    rssdid = models.IntegerField(db_column="RSSDHCR",
                                       verbose_name="RSSDID - High Regulatory Holder",
                                       help_text="The unique number assigned by the Federal Reserve Board to the regulatory high holding company of the institution.")

    reg_holding_state = models.CharField(db_column="STALPHCR",
                                max_length=2,
                                verbose_name="Regulatory holding company state",
                                help_text="State location of the regulatory high holding company (either direct or indirect owner).")

    interstate_branches = models.BooleanField(db_column="STMULT",
                                       verbose_name="Interstate Branches",
                                       help_text="A 'yes' indicates that an institution has branches that can accept "
                                                 "FDIC-insured deposits in more than one state.  "
                                                 "The FDIC Act defines state as any State of the United States, "
                                                 "the District of Columbia, and any territory of the United States, "
                                                 "Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific "
                                                 "Islands, the Virgin Island, and the Northern Mariana Islands.")

    subchapter_s_corp = models.BooleanField(db_column="SUBCHAPS",
                                       verbose_name="Subchapter S Corporations",
                                       help_text="The Small Business Job Protection Act of 1996 changed the "
                                                 "Internal Revenue Code to allow financial institutions to elect "
                                                 "Subchapter S corporation status, beginning in 1997. "
                                                 "Banks are required to indicate on the Call Report whether "
                                                 "there is currently in effect an election to file under Subchapter "
                                                 "S. Thrifts have a similar requirement as of March 1998.  "
                                                 "The most important IRS requirements to elect and maintain "
                                                 "Subchapter S status are: "
                                                 "There can be no more than 75 eligible shareholders and no more than "
                                                 "one class of stock. (In general, shareholders can only be individuals,"
                                                 " estates, and certain types of trusts. Certain retirement plans and "
                                                 "charitable organizations will be eligible in 1998.) All shareholders "
                                                 "must consent.  Banks and thrifts converting to Subchapter S status "
                                                 "must use the specific charge-off method for tax purposes rather than "
                                                 "the reserve method of accounting for bad debts and recapture tax bad "
                                                 "debt reserves over a period of six years, if the reserve method had "
                                                 "been used prior to conversion. "
                                                 "(Note: even though the specific charge-off method is required for tax "
                                                 "purposes, an adequate allowance for loan and lease losses must still "
                                                 "be maintained on the financial statements and Call Reports.) "
                                                 "Banks and thrifts are subject to a built-in gains (BIG) tax, if the "
                                                 "aggregate fair market value of assets is greater than their aggregate "
                                                 "adjusted bases on the date of conversion to Subchapter S status.     "
                                                 "[Banks are required to indicate separately on the Call Report in "
                                                 "December of each year, the deferred portion of income taxes reported "
                                                 "in net income. For Subchapter S banks, some or all of their deferred "
                                                 "tax assets and liabilities may be eliminated upon conversion to "
                                                 "Subchapter S status; however, deferred taxes related to the BIG tax "
                                                 "and the recapture of bad debt reserves must be recognized.].   "
                                                 "A Subchapter S corporation is treated as a pass-through entity, "
                                                 "similar to a partnership, for federal income tax purposes. "
                                                 "It is generally not subject to any federal income taxes at the "
                                                 "corporate level. Its taxable income flows through to its "
                                                 "shareholders in proportion to their stock ownership, "
                                                 "and the shareholders generally pay federal income taxes on their "
                                                 "share of this taxable income. This can have the effect of reducing "
                                                 "institutions' reported income tax expense and increasing their "
                                                 "after-tax earnings..   The election of Subchapter S status may result "
                                                 "in an increase in shareholders' personal tax liabilities. Therefore, "
                                                 "S corporations typically increase the amount of earnings distributed "
                                                 "as dividends to compensate for higher personal taxes.")

    frederal_reserve_district = models.BooleanField(db_column="FDICSUPV",
                                       verbose_name="Federal Reserve District",
                                       help_text="The Federal Reserve District in which the institution is physically located. There are twelve Federal Reserve Districts, with two Districts serving one state in some instances. The list of Federal Reserve Districts and their respective states are as follows: Boston - Connecticut, Maine, Massachuestts, New Hampshire, Rhode Island, Vermont New York - Connecticut, New Jersey, New York, Puerto Rico U.S. Virgin Islands  Phildelphia - Delaware, New Jersey, Pennsylvania Cleveland - Kentucky, Ohio, Pennsylvania, West Virginia Richmond - Maryland, North Carolina, South Carolina, Virginia, West Virginia Atlanta - Alabama, Florida, Georgia, Louisiana, Mississippi, Tennessee Chicago - Illinois, Indiana, Iowa, Michigan, Wisconsin St. Louis - Arkansas, Illinois, Indiana, Kentucky, Mississippi, Missouri, Tennessee Minneapolis - Michigan, Minnesota, Montana, North Dakota, South Dakota, Wisconsin Kansas City - Colorado, Kansas, Missouri, Nebraska, New Mexico, Oklahoma, Wyoming Dallas - Louisiana, New Mexico, Texas San Francisco> - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Nevada, Oregon, States of Micronesia, Utah, Washington ")

    parcert = models.IntegerField(db_column="PARCERT",
                               verbose_name="Directly owned by another bank (CERT)",
                               help_text="The PARCERT number identifies the subsidiary institutions parent certificate number. Beginning in March 1997, both the Thrift Financial Reports and Call Reports are completed on a fully consolidated basis.  Previously, the consolidation of subsidiary depository institutions was prohibited.  Now, parent institutions are required to file consolidated reports, while their subsidiary financial institutions are still required to file separate reports.")

    pretax_roa = models.FloatField(db_column="ROAPTX",
                            verbose_name="Pretax return on assets",
                            help_text="Annualized pre-tax net income as a percent of average assets. Note: Includes extraordinary items and other adjustments, net of taxes.")

    quarterly_pretax_roa = models.FloatField(db_column="ROAPTXQ",
                            verbose_name="Quarterly Pretax return on assets",
                            help_text="Quarterly pre-tax net income as a percent of average assets. Note: Includes extraordinary items and other adjustments, net of taxes.")

    trust = models.BooleanField(db_column="TRUST",
                                       verbose_name="Trust Powers",
                                       help_text="A flag used to indicate an institution's Trust Powers Granted status. 0 = No Trust Power Granted 1 = Trust Power Granted Where Trust Power has been granted specific codes are: 00 - Trust powers not know 10 - Full trust powers granted 11 - Full trust powers granted, exercised 12 - Full trust powers granted, not exercised 20 - Limited trust powers granted 21 - Limited trust powers granted, exercised 22 - Limited trust powers granted, not exercised 30 - Trust powers not granted 31 - Trust powers not granted, but exercised ")

    certcons = models.IntegerField(db_column="CERTCONS",
                               verbose_name="Directly owned by another bank (CERT)",
                               help_text="FDIC certificate number of the parent bank or savings institution with which the reported institution’s financial data has been consolidated. Beginning in March 1997, both the Thrift Financial Reports and Call Reports are completed on a fully consolidated basis.  Previously, the consolidation of subsidiary depository institutions was prohibited.  Now, parent institutions are required to file consolidated reports, while their subsidiary financial institutions are still required to file separate reports.  Click on the certificate number to identify the parent bank or thrift.")


    msa_number = models.IntegerField(db_column="MSA_NO",
                               verbose_name="Metropolitan Statistical Area Number",
                               help_text="The Metropolitan Statistical Area Number (MSA_NO) in which the institution is physically located.  The Office of Managment and Budget defines MSAs in terms of entire counties surrounding central cities, except in the six New England states where they are defined in terms of cities and towns within counties. Before 200 standards")


    asset_concentration_code = models.ForeignKey(Asset_Concentration,
                                   on_delete=models.DO_NOTHING,
                                   db_column="SPECGRP",
                                   verbose_name="Asset Concentration Hierarchy Code",
                                   help_text="An indicator of an institution's primary specialization in terms of asset concentration")

    asset_concentration_name = models.CharField(db_column="SPECGRPN", max_length=255,
                                   verbose_name="Asset Concentration Hierarchy Name",
                                   help_text="An indicator of an institution's primary specialization in terms of asset concentration")

    unique_number = models.IntegerField(db_column="UNINUM",
                               verbose_name="FDIC's unique number",
                               help_text="FDIC's unique identifier number for holding companies, banks, branches and nondeposit subsidiaries.")

    csa = models.CharField(db_column="CSA",
                                max_length=255,
                                verbose_name="Name of the Combined Statistical Area",
                                help_text="The name associated with the numeric code that the U.S. Census Bureau Office of Management and Budget assigns for the combined statistical area (CSA) per the 2000 standards. If an institution is not defined as a CSA, the value of the field will be blank. For more information see: http://site.census.gov/population/site/estimates/metroarea.html .")

    csa_number = models.IntegerField(db_column="CSA_NO",
                               verbose_name="Numeric Code for the Combined Statistical Area",
                               help_text="The numeric code that the U.S. Census Bureau Office of Management and Budget assigns for the combined statistical area (CSA) per the 2000 standards. If an institution is not defined as a CSA, the value of the field will be zero.  For more information see: http://site.census.gov/population/site/estimates/metroarea.html.")

    csa_flag = models.BooleanField(db_column="CSA_FLG",
                                       verbose_name="CSA Area Flag",
                                       help_text="A flag used to indicate whether an institution is in a Combined Statistical Area. 1=yes and 0=no.")

    cbsa = models.CharField(db_column="CBSA",
                                max_length=255,
                                verbose_name="Name of the Core Based Statistical Area",
                                help_text="The name associated with the numeric code that the U.S. Census Bureau Office of Management and Budget assigns for the CBSA. The 2000 standards provide that each CBSA must contain at least one urban area of 10,000 or more population.  Metropolitan and micropolitan statistical areas are two categories of core based statistical areas. If an institution is not defined as a CBSA, the value of the field will be zero. For more information see: http://site.census.gov/population/site/estimates/metroarea.html.")

    cbsa_number = models.IntegerField(db_column="CBSA_NO",
                               verbose_name="Numeric Code for the Core Based Statistical Area",
                               help_text="The numeric code that the U.S. Census Bureaus Office of Management and Budget assigns for the CBSA. The 2000 standards provide that each CBSA must contain at least one urban area of 10,000 or more population.  Metropolitan and micropolitan statistical areas are two"
                                            "categories of core based statistical areas. If an institution is not defined as a CBSA, the value of the field will be zero. For more information see: http://site.census.gov/population/site/estimates/metroarea.html.")

    cbsa_metro_flag = models.BooleanField(db_column="CBSA_METRO_FLG",
                                       verbose_name="Metro Statistical Area Flag",
                                       help_text="A flag used to indicate whether an institution is in a metropolitan statistical area. The US Census bureau office of Management and Budget defines the metropolitan statistical area. A core based statistical area associated with at least one urbanized area that has a population of at least 50,000. The metropolitan statistical area comprises the central county or counties containing the core, plus adjacent outlying counties having a high degree of social and economic integration with the central county as measured through commuting. 0 = institution is not in a metropolitan statistical area or 1 = institution is in a metropolitan statistical area. For more information see: http://site.census.gov/population/site/estimates/metroarea.html .")

    cbsa_micro_flag = models.BooleanField(db_column="CBSA_MICRO_FLG",
                                       verbose_name="Micro Statistical Area Flag",
                                       help_text="A flag used to indicate whether an institution is in a micropolitan statistical area The U.S. Census Bureau Office of Management and Budget defines the micropolitan statistical area. The 2000 standards for a core based statistical area associated with at least one urban cluster that has a population of at least 10,000 but less than 50,000. The micropolitan statistical area comprises the central county or counties containing the core, plus adjacent outlying counties having a high degree of social and economic integration with the central county as measured through commuting. 0 = institution is not in a micropolitan statistical area or 1 = institution is in a micropolitan statistical area. For more information see:  http://site.census.gov/population/site/estimates/metroarea.html .")

    cbsa_div = models.CharField(db_column="CBSA_DIV",
                                max_length=255,
                                verbose_name="Name of the Core Based Statistical Division",
                                help_text="The name associated with the numeric code given by the US Census Bureau office of Management and Budget (2000 standards) that represents the core based statistical division (CBSADIV). A metropolitan division is a county or group of counties within a core based statistical area that contains a core with a population of at least 2.5 million. A CBSA metropolitan division consists of one or more main/secondary counties that represent an employment center or centers, plus adjacent counties associated with the main county or counties through commuting ties. If an institution is not defined as a CBSA division the value of the field will be zero.")

    cbsa_div_number = models.IntegerField(db_column="CBSA_DIV_NO",
                               verbose_name="Core Based Statistical Division Number",
                               help_text="The numeric code given by the US Census Bureau office of Management and Budget that represents the core based statistical division (CBSADIV)under the year 2000 standards. A metropolitan division is a county or group of counties within a core based statistical area that contains a core with a population of at least 2.5 million. A CBSA metropolitan division consists of one or more main/secondary counties that represent an employment center or centers, plus adjacent counties associated with the main county or counties through commuting ties. If an institution is not defined as a CBSA division the value of the field will be zero.")

    cbsa_div_flag = models.BooleanField(db_column="CBSA_DIV_FLG",
                                       verbose_name="CBSA Statistical Area Flag",
                                       help_text="A flag used to indicate whether an institution is in a CBSA division 1=yes, 0=no")

    fund_member = models.BooleanField(db_column="INSDIF",
                                       verbose_name="Deposit Insurance Fund member",
                                       help_text="A flag used to indicate whether an institution is insured under the Deposit Insurance Fund (DIF).  As of April 1, 2006 the Bank Insurance Fund (BIF) was merged together with the Savings Institution Insurance Fund (SAIF) to create a single Deposit Insurance Fund (DIF).  All FDIC insured BIF and SAIF member institutions that are still active or open are now insured members of DIF.    0 = No, not DIF insured and 1 = Yes, DIF insured.  Note that institutions that became inactive prior to April 1006 will also have zero value.")

    class Meta:
        managed = False
        db_table = "fdic_institutions"
        verbose_name = "Institution"

    def __str__(self):
        return self.name