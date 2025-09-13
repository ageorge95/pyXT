from setuptools import setup, find_packages

VERSION = '1.0.2'
DESCRIPTION = 'XT Exchange python wrapper'
LONG_DESCRIPTION = 'Various scripts that can be used to easily interact with the XT exchange.'

setup(
    name="XT",
    version=VERSION,
    author="ageorge95",
    author_email="arteni.george.daniel@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests"
    ],
    extras_require={},
    keywords=['python', 'pyXT', 'XT']
)