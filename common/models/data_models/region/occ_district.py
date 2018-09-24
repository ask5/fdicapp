from django.db import models
from .state import State

# The Office of the Comptroller of the Currency (OCC) District in which the institution is physically located.
# The six OCC Districts and their respective states are:
#
# Northeast - Connecticut, Delaware, District of Columbia, Maine, Maryland, Massachusetts, New Hampshire, New Jersey,
#               New York, Pennsylvania, Puerto Rico, Rhode Island, Vermont, U.S. Virgin Islands
# Southeast - Alabama, Florida, Georgia, Mississippi, North Carolina, South Carolina, Tennessee, Virginia,
#               West Virginia
# Central   - Illinois, Indiana, Kentucky, Michigan, Ohio, Wisconsin
# Midwest   - Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota
# Southwest - Arkansas, Louisiana, New Mexico, Oklahoma, Texas
# West      - Alaska, American Samoa, Arizona, California, Colorado, Guam, Hawaii, Idaho, Montana, Nevada, Oregon,
#               States of Micronesia, Utah, Washington, Wyoming

class OCC_District(models.Model):
    id = models.IntegerField(primary_key=True, db_column="id", verbose_name="Id")
    name = models.CharField(db_column="Name", max_length=50, verbose_name="Name")

    class Meta:
        managed = False
        db_table = "fdic_occ_districts"
        verbose_name = "OCC District"
        ordering =  ['name']

    def __str__(self):
        return self.name

class OCC_District_State(models.Model):
    occ_district_id = models.ForeignKey(OCC_District,
                                        on_delete=models.DO_NOTHING,
                                        db_column="district_id",
                                        verbose_name="OCC District Id")
    state = models.ForeignKey(State,
                              on_delete=models.DO_NOTHING,
                              db_column="state",
                              verbose_name="State Abbreviation")

    class Meta:
        managed = False
        verbose_name = "OCC District - State"
        db_table = "fdic_occ_districts_states"