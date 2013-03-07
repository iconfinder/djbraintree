from django.conf import settings


def braintree_client_side_encryption_key(request):
    return {
        'BRAINTREE_CLIENT_SIDE_ENCRYPTION_KEY':
        getattr(settings, 'BRAINTREE_CLIENT_SIDE_ENCRYPTION_KEY', None),
    }
