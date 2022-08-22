"""
Copyright (c) 2022 Patryk Orzechowski | Wagenaar Lab | University of Pennsylvania
"""

from setuptools import setup, Extension

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="pennsieve2",
    version="0.0.3",
    author="Patryk Orzechowski",
    author_email=("patryk.orzechowski@gmail.com"),
    url="https://github.com/Pennsieve/pennsieve-agent-python",
    description="Pennsieve Python Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=True,
    install_requires=["grpcio", "grpcio-tools", "protobuf"],
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
