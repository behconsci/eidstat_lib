try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    with open('README.rst') as file:
        long_description = file.read()
except IOError:
    long_description = 'Python lib for eidstat.com'

setup(
    name='eidstat',
    packages=['eidstat'],
    version='0.1',
    long_description=long_description,
    description='Python lib for eidstat.com',
    author='Doniyor Jurabayev',
    author_email='behconsci@gmail.com',
    url='https://github.com/behconsci/eidstat_lib',
    download_url='https://github.com/behconsci/eidstat_lib/archive/0.1.zip',
    keywords=['track', 'monitor', 'bug'],
    classifiers=[],
    install_requires=[
        'requests', 'grequests'
    ],
)
