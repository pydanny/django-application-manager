from setuptools import setup, find_packages
 
version = '0.1'
 
LONG_DESCRIPTION = """
=======================================================
django-application-manager (Django Application Manager)
=======================================================

A tool designed to let site admins and users manage what
applications they are currently using.

This was originally created for Pinax, but I've kept things as loosely coupled 
to other modules as possible. It should work with other Django efforts, but so
far it only has been tested against Pinax.


Using django-application-manager
================================
1. Install as application_manager in your Django apps directory.
2. Do database stuff     


"""
 
setup(
    name='django-application-manager',
    version=version,
    description="django-application-manager",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='pinax,django',
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='http://django-application-manager.googlecode.com/',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
