#!/usr/bin/env python
from distutils.core import setup

setup(
    name='OpenPrecincts',
    version='0.1',
    author='Michal Migurski',
    packages=['OpenPrecincts'],
    install_requires=['GDAL>=2', 'geopandas>=0.4', 'pandas'],
    )
