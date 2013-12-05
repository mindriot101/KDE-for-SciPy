from setuptools import setup
import os
import sys

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
        name='scikde',
        version='0.1.1',
        description='Kernel Density Estimation (KDE) for scipy',
        author='Daniel B Smith',
        author_email='',
        maintainer='Simon Walker',
        maintainer_email='s.r.walker101@googlemail.com',
        url='https://github.com/mindriot101/KDE-for-SciPy',
        packages=['scikde',],
        install_requires=['scipy'],
        )
