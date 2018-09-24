from django.db import models

# A classification code assigned by the FDIC based on the institution's
#"charter type (commercial bank or savings institution), charter agent "
#"(state or federal), Federal Reserve membership status "
#"(Fed member, Fed nonmember)and its primary federal regulator "
#"(state chartered institutions are subject to both federal and state "
#"supervision). N = commercial bank, national (federal) charter and Fed member"
#", supervised by the Office of the Comptroller of the Currency (OCC)."
#"SM = commercial bank, state charter and Fed member, supervised by the "
#"Federal Reserve (FRB). NM = commercial bank, state charter and "
#"Fed nonmember, supervised by the FDIC  SB = savings banks, state charter, "
#"supervised by the FDIC. SA = savings associations, state or federal charter,"
#"supervised by the Office of Thrift Supervision (OTS). "
#"OI = insured U.S. branch of a foreign chartered institution (IBA).

class Charter_Class(models.Model):
    code = models.CharField(primary_key=True, db_column="ClassCode", verbose_name="Class Code", max_length=10)
    description = models.CharField(db_column="Description", max_length=255, verbose_name="Description")

    class Meta:
        managed = False
        db_table = "fdic_charter_classes"
        ordering = ['description']
        verbose_name = "Charter Class"
        verbose_name_plural = "Charter Classes"

    def __str__(self):
        return self.description