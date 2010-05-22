import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
setup(
    name='django-fortunes',
    version='0.2.0',
    description="Django Fortunes",
    long_description=read('README.markdown'),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='social,fortunes,django',
    author='Nicolas Perriault',
    url='http://github.com/n1k0/djortunes/tree/master',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)