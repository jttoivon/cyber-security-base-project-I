# Define signal handlers for the login, logout, and failed login events
# https://stackoverflow.com/questions/37618473/how-can-i-log-both-successful-and-failed-login-and-logout-attempts-in-django/37620866#37620866

import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

log = logging.getLogger("notes")

log.info("Executed the signals module")

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):    
    # to cover more complex cases:
    # http://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
    ip = request.META.get('REMOTE_ADDR')

    log.info('login user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs): 
    ip = request.META.get('REMOTE_ADDR')

    log.info('logout user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):
    log.info('login failed for: {credentials}'.format(
        credentials=credentials,
    ))
