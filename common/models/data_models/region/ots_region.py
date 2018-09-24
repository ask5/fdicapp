from django.db import models
from .state import State

# Prior to 7/21/11, the Office of Thrift Supervision (OTS) Region in which the institution is physically located.
# The five OTS Regions and their respective states are:
# Northeast - Connecticut, Delaware, Maine, Massachusetts, New Hampshire, New Jersey, New York, Pennsylvania,
#               Rhode Island, Vermont, West Virginia
# Southeast - Alabama, District of Columbia, Florida, Georgia, Maryland, North Carolina, Puerto Rico,
#               South Carolina, U.S. Virgin Islands, Virginia
# Central   - Illinois, Indiana, Kentucky, Michigan, Ohio, Tennessee, Wisconsin
# Midwest   - Arkansas, Colorado, Iowa, Kansas, Louisiana, Minnesota, Mississippi, Missouri, Nebraska,
#               New Mexico, North Dakota, Oklahoma, South Dakota, Texas
# West      - Alaska, American Samoa, Arizona, California, Guam, Hawaii, Idaho, Montana, Nevada, States of Micronesia,
#               Oregon, Utah, Washington, Wyoming


class OTS_Region(models.Model):
    name = models.CharField(primary_key=True, db_column="Name", max_length=50, verbose_name="Name")

    class Meta:
        managed = False
        db_table = "fdic_ots_regions"
        verbose_name = "OTS Region"

    def __str__(self):
        return self.name


class OTS_Region_State(models.Model):
    id = models.AutoField(primary_key=True)
    region = models.ForeignKey(OTS_Region,
                                  on_delete=models.DO_NOTHING,
                                  db_column="region",
                                  verbose_name="OTS Region")

    state = models.ManyToManyField(State, db_column="state",
                              verbose_name="State Abbreviation")

    class Meta:
        managed = False
        verbose_name = "OTS Region - State"
        db_table = "fdic_ots_region_states"