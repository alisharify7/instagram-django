from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

def get_next_page(request):
    nxt = request.GET.get("next", None)
    if nxt is None:
        return settings.LOGIN_REDIRECT_URL
    elif not url_has_allowed_host_and_scheme(
            url=nxt,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()):
        return settings.LOGIN_REDIRECT_URL
    else:
        return nxt