import braintree
from django.conf import settings
from django.test.signals import setting_changed
from django.dispatch import receiver
from django.core.exceptions import ImproperlyConfigured


def configure():
    """(Re-)configure Braintree from the Django settings.

    :raises django.core.exceptions.ImproperlyConfigured:
        if one of the required settings are not set.
    """

    if not hasattr(settings, 'BRAINTREE_ENVIRONMENT'):
        raise ImproperlyConfigured(
            'No Braintree environment configured for the application. Please '
            'set the `BRAINTREE_ENVIRONMENT` setting'
        )
    if not hasattr(settings, 'BRAINTREE_MERCHANT_ID'):
        raise ImproperlyConfigured(
            'No Braintree merchant ID configured for the application. Please '
            'set the `BRAINTREE_MERCHANT_ID` setting'
        )
    if not hasattr(settings, 'BRAINTREE_PUBLIC_KEY'):
        raise ImproperlyConfigured(
            'No Braintree public key configured for the application. Please '
            'set the `BRAINTREE_PUBLIC_KEY` setting'
        )
    if not hasattr(settings, 'BRAINTREE_PRIVATE_KEY'):
        raise ImproperlyConfigured(
            'No Braintree private key configured for the application. Please '
            'set the `BRAINTREE_PRIVATE_KEY` setting'
        )

    braintree.Configuration.configure(settings.BRAINTREE_ENVIRONMENT,
                                      settings.BRAINTREE_MERCHANT_ID,
                                      settings.BRAINTREE_PUBLIC_KEY,
                                      settings.BRAINTREE_PRIVATE_KEY)
    braintree.Configuration.use_unsafe_ssl = \
        getattr(settings, 'BRAINTREE_USE_UNSAFE_SSL', False)


@receiver(setting_changed)
def setting_changed_callback(sender, **kwargs):
    """Reconfigure Braintree when settings are changed during testing.
    """

    configure()


configure()
