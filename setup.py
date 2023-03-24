from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in indiamart_integration/__init__.py
from indiamart_integration import __version__ as version

setup(
	name="indiamart_integration",
	version=version,
	description="indiamart_integration",
	author="Dhruvi",
	author_email="dhruvikaneriya52@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
