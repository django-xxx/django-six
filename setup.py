# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.2'


setup(
    name='django-six',
    version=version,
    keywords='django-six',
    description='Django-six —— Django Compatibility Library',
    long_description=open('README.rst').read(),

    url='https://github.com/Brightcells/django-six',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=[],
    py_modules=['django_six', ],
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
