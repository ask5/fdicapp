from django.db import models
from .state import State


#
# The supervisory FDIC office assigned to the institution.
# The eight FDIC Supervisory Regions and their respective states are:
#
# Boston        - Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont
# New York      - Delaware, District of Columbia, Maryland, New Jersey, New York, Pennsylvania, Puerto Rico,
#                 U.S. Virgin Islands
# Atlanta       - Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia, West Virginia
# Memphis       - Arkansas, Kentucky, Louisiana, Mississippi, Tennessee
# Chicago       - Illinois, Indiana, Michigan, Ohio, Wisconsin
# Kansas City   - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota
# Dallas        - Colorado, New Mexico, Oklahoma, Texas
# San Francisco - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, Oregon,
#                 States of Micronesia, Utah, Washington, Wyoming
#

class Supervisory_Region(models.Model):
    name = models.CharField(primary_key=True, db_column="Name", max_length=50, verbose_name="Name")

    class Meta:
        managed = False
        db_table = "fdic_supervisory_regions"
        verbose_name = "Supervisory Region"

    def __str__(self):
        return self.name

class Supervisory_Region_State(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(Supervisory_Region,
                                  on_delete=models.DO_NOTHING,
                                  db_column="region",
                                  verbose_name="Supervisory Region")

    state = models.ManyToManyField(State, db_column="state",
                                   verbose_name="State Abbreviation")

    class Meta:
        managed = False
        db_table = "fdic_supervisory_region_states"
        verbose_name = "Supervisory Region - State"