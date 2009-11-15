#!/usr/bin/env python

from distutils.core import setup

app_name = 'twitter'

setup(name='django-%s' % app_name,
        version='0.9.0',
        packages=[app_name, '%s.templatetags' % app_name],
        author = 'Joshua Partogi',
        author_email = 'joshua.partogi@gmail.com',
        url = 'http://github.com/scrum8/django-twitter/',
        download_url = 'http://github.com/scrum8/django-twitter/archives/master/',

        license = "BSD License",
        keywords = "django twitter",
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Application Frameworks',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        platforms = ['any'],
)