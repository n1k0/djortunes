Djortunes (`django_fortunes` app)
=================================

`django_fortunes`'s a [Django](http://www.djangoproject.com/) application to store fortunes (snippets of quotes, eg. IRC/IM ones). Originally inspired by the « [Fortunes](http://fortunes.inertie.org/) » application, by [Maurice Svay](http://svay.com/).

![screenshot](http://files.droplr.com/files/6619162/RKP6D.djortunes.png "Example app screen")

I'm discovering and learning both [Python](http://python.org/) and [Django](http://www.djangoproject.com/) while coding it, so don't expect too much reliability, but I would warmly welcome any code review against the code :)

If you're curious enough, you might check out the [Symfony version of this app](http://github.com/n1k0/sftunes). 

Prerequisites
-------------

* Django 1.2 or more recent
* `django-registration` 0.7
* Eventually, the `django-debug-toolbar`

Installation
------------

Djortunes ship as a standalone application (located in the `django_fortunes` directory), and a sample Django project is also provided as an example of use (in the `django_fortunes_example` directory).

The better way to install dependencies (using a `virtualenv` is highly encouraged) is by using the provided `pip` requirements file:

    $ pip install -r requirements.txt

Then, just run the `./manage.py runserver` within the `django_fortunes_example` directory:

    $ cd django_fortunes_example
    $ ./manage.py runserver

Configuration
-------------

Several settings are available in the `django_fortunes` application, and you can override their defaults in your project's `settings.py` configuration file:

    # Maximum number of fortunes to be shown in lists
    FORTUNES_MAX_PER_PAGE = 10

    # Maximum number of top fortune authors to display in the sidebar
    FORTUNES_MAX_TOP_CONTRIBUTORS = 5

License
-------

This work is released under the terms of the [MIT license](http://en.wikipedia.org/wiki/MIT_License).

Authors
-------

* [Nicolas Perriault](http://github.com/n1k0)
* [Florent Messa](http://github.com/thoas)
