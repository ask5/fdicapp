from django.db import models
from .state import State

# The Quarterly Banking Profile (QBP) Commercial Bank Region in which the institution is physically located.
# Atlanta - Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia, West Virginia
# Chicago - Illinois, Indiana, Kentucky, Michigan, Ohio, Wisconsin
# Dallas - Arkansas, Colorado, Louisiana, Mississippi, New Mexico, Oklahoma, Tennessee, Texas
# Kansas City - Iowa, Kansas, Minnesota, Missouri, North Dakota, Nebraska, South Dakota
# New York - Connecticut, District of Columbia, Delaware, Maine, Maryland, Massachusetts, New Hampshire, New Jersey,
#           New York, Pennsylvania, Puerto Rico, Rhode Island, Vermont, U.S. Virgin Islands
# San Francisco - Alaska, American Samoa, Arizona, California, States of Micronesia, Hawaii, Idaho, Montana, Nevada,
#       Oregon, Utah, Washington, Wyoming, Guam, States of Micronesia



class QBP_Region(models.Model):
    id = models.IntegerField(primary_key=True, db_column="id", verbose_name="Id")
    name = models.CharField(db_column="Name", max_length=50, verbose_name="Name")

    class Meta:
        managed = False
        db_table = "fdic_qbp_regions"
        verbose_name = "Quarterly Banking Profile (QBP) Region"

    def __str__(self):
        return self.name

class QBP_Region_State(models.Model):
    id = models.AutoField(primary_key=True)
    region_id = models.ForeignKey(QBP_Region,
                                  on_delete=models.DO_NOTHING,
                                  db_column="region_id",
                                  verbose_name="QBP Region Id")

    state = models.ManyToManyField(State, db_column="state",
                                   verbose_name="State Abbreviation")

    class Meta:
        managed = False
        db_table = "fdic_qbp_region_states"
        verbose_name = "QBP Region - State"