"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

import codecs
import os.path

from setuptools import setup, Extension, find_packages
from pennsieve2 import __version__


with open("README.md", "r") as fh:
    long_description = fh.read()




setup(
    name="pennsieve2",
#    version=get_version('__init__.py'),
    version=__version__,
    author="Patryk Orzechowski",
    author_email=("patryk.orzechowski@gmail.com"),
    url="https://github.com/Pennsieve/pennsieve-agent-python",
    description="Pennsieve Python Client",
    packages=find_packages(),
    package_data={'pennsieve2': ['pennsieve2/protos/*.proto']},
    package_dir={'pennsieve2' : 'pennsieve2'},
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=True,
    install_requires=["grpcio>=1.45.0", "protobuf"],
    extras_require={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    keywords=["pennsieve", "data science", "datasets", "repositories"],
)
