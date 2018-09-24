from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models.system_models import *

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserDetailInline(admin.StackedInline):
    model = UserDetail
    can_delete = False
    verbose_name_plural = 'user details'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserDetailInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address1', 'city', 'state', 'state', 'is_active')
admin.site.register(Customer, CustomerAdmin)


class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'first_name', 'last_name', 'phone', 'email')
admin.site.register(ContactPerson, ContactPersonAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('sub_id', 'customer_id', 'start_date', 'end_date', 'auto_renew', 'is_trial', 'is_active')
admin.site.register(Subscription, SubscriptionAdmin)

class SubscriptionUserAdmin(admin.ModelAdmin):
    list_display = ('sub_id', 'user_id', 'create_date')
admin.site.register(Subscription_User, SubscriptionUserAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_active', 'enable_trial')
admin.site.register(Product, ProductAdmin)

class FeatureTagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'name', 'description', 'is_active')
admin.site.register(FeatureTags, FeatureTagsAdmin)


class Product_FeatureAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'feature_id')
admin.site.register(Product_Feature, Product_FeatureAdmin)

