===============================
Python Library for eidstat.com
===============================

Install
-------

``pip install eidstat``


Usage
-----

::

    from eidstat import Stat

    et = Stat(token='ave32sde98ruj23if3riugrg')

    et.watch('important event')


In Django Project, it is better to setup in settings.py and call the event tracker in views or wherever you want