Braintree for Django
====================

``djbraintree`` easily integrates the official `Braintree Python client library <https://github.com/braintree/braintree_python>`_ into your Django applications by allowing easy configuration from your Django settings.


Quick start
-----------

1.  Install ``djbraintree`` from PyPI:

    ::
    
       $ pip install djbraintree

2.  Update your project's ``settings.py``:

    ::
    
       INSTALLED_APPS = (
           ..
           'django_barintree',
       )
       
       TEMPLATE_CONTEXT_PROCESSORS = (
           ..
           'djbraintree.context_processsors.braintree_client_side_encryption_key',
       )
       
       import braintree
       
       BRAINTREE_ENVIRONMENT = braintree.Environment.Sandbox
       BRAINTREE_CLIENT_SIDE_ENCRYPTION_KEY = '..'
       BRAINTREE_MERCHANT_ID = '..'
       BRAINTREE_PUBLIC_KEY = '..'
       BRAINTREE_PRIVATE_KEY = '..'

3.  Start using the Braintree Python client library in your code:

    ::
    
       import braintree
       
       result = braintree.Transaction.sale({
           "amount": "1000.00",
           "credit_card": {
               "number": "4111111111111111",
               "expiration_date": "05/2012"
           }
       })


Configuration options
---------------------

``BRAINTREE_ENVIRONMENT``
    Braintree environment. Refer to `the Braintree Python client library documentation <https://braintree_python.readthedocs.org/en/latest/environment.html>`_ for more details.
``BRAINTREE_CLIENT_SIDE_ENCRYPTION_KEY``
    Optional client side encryption key. Will be exposed using the ``braintree_client_side_encryption_key`` context processor as ``BRAINTREE_CLIENT_SIDE_ENCRYPTION_KEY`` in your templates if set.
``BRAINTREE_MERCHANT_ID``
    Merchant ID.
``BRAINTREE_PUBLIC_KEY``
    Public key.
``BRAINTREE_PRIVATE_KEY``
    Private key.
``BRAINTREE_USE_UNSAFE_SSL``
    Allow unsafe SSL connections. Default ``False`` and highly discouraged.
