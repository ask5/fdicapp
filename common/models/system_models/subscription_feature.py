from django.db import models
from .subscription import Subscription
from .feature_tags import FeatureTags
from .product import Product

class Subscription_Feature(models.Model):

    TYPES = (
        ('P', 'Product'),
        ('A', 'Add-On'),
    )
    id = models.AutoField(primary_key=True)
    sub_id = models.ForeignKey(Subscription, db_column="sub_id", on_delete=models.DO_NOTHING)
    feature_id = models.ForeignKey(FeatureTags, db_column="feature_id", on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=1, choices=TYPES, default='P')
    product_id = models.ForeignKey(Product, db_column="product_id", on_delete=models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified"
                                         ,blank=True, null=True)

    class Meta:
        managed = False
        db_table = "system_subscription_features"
        verbose_name = "Subscription Feature"
        verbose_name_plural = "Subscription Features"
