from django.db import models
from .product import Product
from .feature_tags import FeatureTags

class Product_Feature(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, db_column="product_id", on_delete=models.DO_NOTHING)
    feature_id = models.ForeignKey(FeatureTags, db_column="feature_id", on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(db_column="create_date", auto_now_add=True, verbose_name="Create Date")
    modified_date = models.DateTimeField(db_column="modified_date", auto_now=True, verbose_name="Last Modified", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "system_product_features"
        verbose_name = "Product Feature"
        verbose_name_plural = "Product Features"
