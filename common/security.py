from .models.system_models import *


class Security():

    def get_user_profile(self, user):
        p = None
        if user:
            s = Subscription_User.objects.filter(user_id=user.id)
            if s:
                p = {
                    'subscription': s
                }
        return p

    def cache_key(self,user):
        return "security:{}".format(str(user.id))