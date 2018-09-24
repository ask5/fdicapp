from django.db import models

from .misc import Office_Type
from .regulatory import *


class Office(models.Model):

    uninum = models.IntegerField(primary_key=True, db_column="UNINUM",
                                 verbose_name="Unique Identification Number for a Branch Office",
                                 help_text="Unique Identification Number for a Branch Office as assigned by the FDIC")

    address = models.CharField(db_column="ADDRESS",
                               max_length=255,
                               verbose_name="Branch Address",
                               help_text="Street address at which the branch is physically located.")

    institution_class =  models.ForeignKey(Charter_Class,
                                db_column="BKCLASS",
                                on_delete=models.DO_NOTHING,
                                verbose_name="Institution Class",
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

    cbsa = models.CharField(db_column="CBSA",
                               max_length=100,
                               verbose_name="Core Based Statistical Area Name (Branch)",
                               help_text="Name of the Core Based Statistical Area (CBSA) as defined by the US Census Bureau Office of Management and Budget.")

    cbsa_division = models.CharField(db_column="CBSA_DIV",
                               max_length=300,
                               verbose_name="Metropolitan Divisions Name (Branch)",
                               help_text="Name of the Core Based Statistical Division as defined by the US Census Bureau Office of Management and Budget.")

    cbsa_division_flag = models.BooleanField(db_column="CBSA_DIV_FLG",
                                          verbose_name="Metropolitan Divisions Flag (Branch)",
                                          help_text="A flag (1=Yes) indicating member of a Core Based Statistical Division as defined by the US Census Bureau Office of Management and Budget.")

    cbsa_division_number = models.IntegerField(db_column="CBSA_DIV_NO",
                                             verbose_name="Metropolitan Divisions Number (Branch)",
                                             help_text="Numeric code of the Core Based Statistical Division as defined by the US Census Bureau Office of Management and Budget.")

    cbsa_metro_number = models.IntegerField(db_column="CBSA_METRO",
                                             verbose_name="Metropolitan Division Number (Branch)",
                                             help_text="Numeric code of the Metropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget")

    cbsa_metro_flag = models.BooleanField(db_column="CBSA_METRO_FLG",
                                          verbose_name="Metropolitan Division Flag (Branch)",
                                          help_text="A flag (1=Yes) used to indicate whether an branch is in a Metropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget")

    cbsa_metro_name = models.CharField(db_column="CBSA_METRO_NAME",
                               max_length=255,
                               verbose_name="Metropolitan Division Name (Branch)",
                               help_text="Name of the Metropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget")

    cbsa_micro_flag = models.BooleanField(db_column="CBSA_MICRO_FLG",
                                          verbose_name="Micropolitan Division Flag (Branch)",
                                          help_text="A flag (1=Yes) used to indicate whether an branch is in a Micropolitan Statistical Area as defined by the US Census Bureau Office of Management and Budget")

    cbsa_number = models.IntegerField(db_column="CBSA_NO",
                                             verbose_name="Core Based Statistical Areas (Branch)",
                                             help_text="Numeric code of the Core Based Statistical Area (CBSA) as defined by the US Census Bureau Office of Management and Budget.")

    cert = models.IntegerField(db_column="CERT",
                            verbose_name="Institution FDIC Certificate #",
                            help_text="A unique number assigned by the FDIC used to identify institutions and for the issuance of insurance certificates.")

    city = models.CharField(db_column="CITY",
                            max_length=75,
                            verbose_name="Branch City",
                            help_text="City in which branch is physically located.")

    county = models.CharField(db_column="COUNTY",
                                max_length=50,
                                verbose_name="Branch County",
                                help_text="County where the branch is physically located.")

    csa = models.CharField(db_column="CSA",
                               max_length=255,
                               verbose_name="Combined Statistical Area Name (Branch)",
                               help_text="Name of the Combined Statistical Area (CSA) as defined by the US Census Bureau Office of Management and Budget")

    csa_flag = models.BooleanField(db_column="CSA_FLG",
                                          verbose_name="Combined Statistical Area Flag (Branch)",
                                          help_text="Flag (1=Yes) indicating member of a Combined Statistical Area (CSA) as defined by the US Census Bureau Office of Management and Budget")

    csa_number = models.IntegerField(db_column="CSA_NO",
                                             verbose_name="Combined Statistical Area Number (Branch)",
                                             help_text="Numeric code of the Combined Statistical Area (CSA) as defined by the US Census Bureau Office of Management and Budget")

    established_date = models.DateTimeField(db_column="ESTYMD",
                                       verbose_name="Branch Established Date",
                                       help_text="The date on which the branch began operations.")

    fi_uninum = models.IntegerField(db_column="FI_UNINUM",
                                             verbose_name="FDIC UNINUM of the Owner Institution",
                                             help_text="This is the FDIC UNINUM of the institution that owns the branch.  A UNINUM is a unique sequentially number added to the FDIC database for both banks and  branches.  There is no pattern imbedded within the number.  The FI_UNINUM is updated with every merger or purchase of branches to reflect the most current owner.")

    main_office = models.BooleanField(db_column="MAINOFF",
                                          verbose_name="Main Office",
                                          help_text="The main office for the institution.")

    institution_name = models.CharField(db_column="NAME",
                               max_length=255,
                               verbose_name="Institution Name",
                               help_text="Legal name of the FDIC Insured Institution")

    office_name = models.CharField(db_column="OFFNAME",
                               max_length=255,
                               verbose_name="Office Name",
                               help_text="Name of Branch")

    office_number = models.IntegerField(db_column="OFFNUM",
                                             verbose_name="Branch Number",
                                             help_text="The branch's corresponding office number.")

    run_date = models.DateTimeField(db_column="RUNDATE",
                                       verbose_name="Run Date",
                                       help_text="The day the institution information was updated.")

    service_type = models.ForeignKey(Office_Type,
                            on_delete=models.DO_NOTHING,
                            db_column="SERVTYPE",
                            verbose_name="Service Type Code",
                            help_text="Define the various types of offices of FDIC-insured institutions.")

    state_abbr = models.CharField(db_column="STALP",
                               max_length=2,
                               verbose_name="Branch State Abbreviation",
                               help_text="State abbreviation in which the branch is physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.")

    state_county_number = models.IntegerField(db_column="STCNTY",
                                             verbose_name="State and County Number",
                                             help_text="A five digit number representing the state and county in which the institution is physically located.  The first two digits represent the FIPS state numeric code and the last three digits represent the FIPS county numeric code.")

    state = models.CharField(db_column="STNAME",
                               max_length=50,
                               verbose_name="Branch State",
                               help_text="State in which the  branch is physically located. The FDIC Act defines state as any State of the United States, the District of Columbia, and any territory of the United States, Puerto Rico, Guam, American Samoa, the Trust Territory of the Pacific Islands, the Virgin Island, and the Northern Mariana Islands.")

    zip = models.CharField(db_column="ZIP",
                               max_length=10,
                               verbose_name="Zip Code",
                               help_text="The first five digits of the full postal zip code representing physical location of the branch.")

    class Meta:
        managed = False
        db_table = "fdic_offices"
        verbose_name = "Office"

    def __str__(self):
        return self.office_name