# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in check_available_qty_from_so/__init__.py
from check_available_qty_from_so import __version__ as version

setup(
	name='check_available_qty_from_so',
	version=version,
	description='Check Available Qty From So',
	author='Bhavesh Maheshwari',
	author_email='maheshwaribhavesh95863@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
