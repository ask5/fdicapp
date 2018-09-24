from django.db import models
from .state import State

# The FDIC Office assigned to the geographic area.
# The eight FDIC Regions and their respective states are:
#
# Boston        - Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont
# New York      - Delaware, District of Columbia, Maryland, New Jersey, New York, Pennsylvania, Puerto Rico,
#                   U.S. Virgin Islands
# Atlanta       - Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia, West Virginia
# Memphis       - Arkansas, Kentucky, Louisiana, Mississippi, Tennessee
# Chicago       - Illinois, Indiana, Michigan, Ohio, Wisconsin
# Kansas City   - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota
# Dallas        - Colorado, New Mexico, Oklahoma, Texas
# San Francisco - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada,
#                   Oregon, States of Micronesia, Utah, Washington, Wyoming

class FDIC_Region(models.Model):
    id = models.IntegerField(primary_key=True, db_column="id", verbose_name="Region Id")
    name = models.CharField(db_column="Name", max_length=50, verbose_name="Name")

    class Meta:
        managed = False
        verbose_name = "Federal Region"
        db_table = "fdic_regions"

    def __str__(self):
        return self.name


class FDIC_Region_State(models.Model):
    id = models.AutoField(primary_key=True)
    region_id = models.ForeignKey(FDIC_Region,
                                  on_delete=models.DO_NOTHING,
                                  db_column="region_id",
                                  verbose_name="Region Id")

    state = models.ForeignKey(State, db_column="state", on_delete=models.DO_NOTHING,
                              verbose_name="State Abbreviation")

    class Meta:
        managed = False
        verbose_name = "Federal Region - State"
        db_table = "fdic_region_states"