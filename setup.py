#!/usr/bin/python3
from setuptools import setuptools, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='csepy',
     version='0.0.1.1',
     author="Yuval Feldman",
     author_email="csepyproject@gmail.com",
     description="A python command service engine package",
     long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/csepy/csepy",
    packages=find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
 )
