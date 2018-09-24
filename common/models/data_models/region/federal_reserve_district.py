from django.db import models
from .state import State

# 01 – Boston, 02 - New York,03 – Philadelphia, 04 – Cleveland,05 – Richmond,06 – Atlanta,07 – Chicago,
# 08 - St. Louis,09 – Minneapolis,10 - Kansas city,11 – Dallas,12 - San Francisco

# "The Federal Reserve District in which the institution is physically located.
# There are twelve Federal Reserve Districts, with two Districts serving one state in some instances.
# The list of Federal Reserve Districts and their respective states are as follows:
# Boston - Connecticut, Maine, Massachuestts, New Hampshire, Rhode Island, Vermont
# New York - Connecticut, New Jersey, New York, Puerto Rico U.S. Virgin Islands
# Phildelphia - Delaware, New Jersey, Pennsylvania
# Cleveland - Kentucky, Ohio, Pennsylvania, West Virginia
# Richmond - Maryland, North Carolina, South Carolina, Virginia, West Virginia
# Atlanta - Alabama, Florida, Georgia, Louisiana, Mississippi, Tennessee
# Chicago - Illinois, Indiana, Iowa, Michigan, Wisconsin
# St. Louis - Arkansas, Illinois, Indiana, Kentucky, Mississippi, Missouri, Tennessee
# Minneapolis - Michigan, Minnesota, Montana, North Dakota, South Dakota, Wisconsin
# Kansas City - Colorado, Kansas, Missouri, Nebraska, New Mexico, Oklahoma, Wyoming
# Dallas - Louisiana, New Mexico, Texas
# San Francisco> - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Nevada, Oregon, States of Micronesia, Utah, Washington "

class Federal_Reserve_District(models.Model):
    id = models.IntegerField(primary_key=True, db_column="id", verbose_name="Id")
    name = models.CharField(db_column="Name", max_length=50, verbose_name="Name")

    class Meta:
        managed = False
        verbose_name = "Federal Reserve District"
        db_table = "fdic_federal_reserve_districts"
        ordering = ['id']

    def __str__(self):
        return self.name


class FRD_State(models.Model):
    id = models.AutoField(primary_key=True)
    district_id = models.ForeignKey(Federal_Reserve_District,
                                  on_delete=models.DO_NOTHING,
                                  db_column="district_id",
                                  verbose_name="District Id")

    state = models.ForeignKey(State, db_column="state", on_delete=models.DO_NOTHING,
                              verbose_name="State Abbreviation")

    class Meta:
        managed = False
        db_table = "fdic_federal_reserve_district_states"
        verbose_name = "Federal Reserve District - State"