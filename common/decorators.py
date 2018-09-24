from django.core.exceptions import PermissionDenied
from .security import Security
from django.core.cache import cache

def subscription_required(function):
    def wrap(request, *args, **kwargs):
        security = Security()
        cache_key = security.cache_key(user=request.user)
        if cache.get(cache_key):
            return function(request, *args, **kwargs)
        else:
            p = security.get_user_profile(user=request.user)
            if p:
                cache.set(cache_key, p)
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap