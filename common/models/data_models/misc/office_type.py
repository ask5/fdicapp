from django.db import models

#Define the various types of offices of FDIC-insured institutions.
#11	Full Service Brick and Mortar Office
#12	Full Service Retail Office
#13	Full Service Cyber Office
#14	Full Service Mobile Office
#15	Full Service Home/Phone Banking
#16	Full Service Seasonal Office
#21	Limited Service Administrative Office
#22	Limited Service Military Facility
#23	Limited Service Facility Office
#24	Limited Service Loan Production Office
#25	Limited Service Consumer Credit Office
#26	Limited Service Contractual Office
#27	Limited Service Messenger Office
#28	Limited Service Retail Office
#29	Limited Service Mobile Office
#30	Limited Service Trust Office

class Office_Type(models.Model):
    id = models.IntegerField(primary_key=True,db_column="id", verbose_name="ID")
    description = models.CharField(db_column="Description", max_length=50, verbose_name="Description")

    class Meta:
        managed = False
        db_table = "fdic_office_types"
        verbose_name = "Office Service Type Code"

    def __str__(self):
        return self.description