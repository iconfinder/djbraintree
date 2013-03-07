from setuptools import setup

setup(
    name='djrill',
    version='0.1.0',
    description='Braintree for Django',
    keywords='django, braintree',
    author='Nick Bruun <nick@bruun.co>',
    author_email='nick@bruun.co',
    url='https://github.com/iconfinder/django_braintree',
    license='BSD License',
    packages=['django_braintree'],
    zip_safe=False,
    install_requires=['braintree', 'django'],
    include_package_data=True,
    test_suite='runtests.runtests',
    tests_require=['nose'],
    classifiers=[
        'Programming Language :: Python', 
        'Programming Language :: Python :: 2.6', 
        'Programming Language :: Python :: 2.7', 
        'Programming Language :: Python :: 3', 
        'Programming Language :: Python :: 3.2', 
        'License :: OSI Approved :: BSD License', 
        'Topic :: Software Development :: Libraries :: Python Modules', 
        'Framework :: Django', 
        'Environment :: Web Environment', 
    ], 
)
