KungFuCode
==========

A gamified version of a code tracking platform.
This is the server side built on Django 1.5 and the django-rest-framework

Create Doxygen
=============
To create the documentation run:
doxygen config.dox

Dependencies
=============

Python 2.7.3
Django 1.5.1

How to install the django rest framework:

pip install djangorestframework
pip install markdown  # Markdown support for the browseable API.
pip install pyyaml    # YAML content-type support.
pip install django-filter  # Filtering support

Run
=======================
First time:
./manage.py syncdb

Run the server:
./manage.py runserrer


Usage
==============================
Assuming you are running the server on yourdomain.com.
URL: yourdomain.com        -> blog for coders
URL: yourdomain.com/admin/ -> admin interface
URL: yourdomain/activity/  -> log of code activity




