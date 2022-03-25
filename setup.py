from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_system_monitor/__init__.py
from frappe_system_monitor import __version__ as version

setup(
	name="frappe_system_monitor",
	version=version,
	description="System monitor for frappe and ERPNExt",
	author="Anthony Emmanuel",
	author_email="hackacehuawei@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
