#!/usr/bin/env python
from distutils.core import setup

setup(
    name='OpenPrecincts',
    version='0.1.1',
    author='Michal Migurski',
    packages=['OpenPrecincts'],
    install_requires=['GDAL>=2', 'geopandas>=0.4', 'pandas'],
    extras_require = {
        'preview': ['matplotlib>=3', 'contextily', 'mercantile'],
        },
    entry_points = dict(
        console_scripts = [
            'openprec-preview-feed = OpenPrecincts.preview:main_feed',
            'openprec-validate-feed = OpenPrecincts.validate:main',
            ]
        ),
    )
