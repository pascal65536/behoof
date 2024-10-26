DESCRIPTION = """
Copyright (C) 2020-2024 Sergey V. Pakhtusov (pascal65536@gmail.com)
Module for handling JSON data in Python.
"""


from setuptools import find_namespace_packages, setup, find_packages

setup(
    name="utilspascal65536",
    version="1.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Sergey V. Pakhtusov",
    author_email="pascal65536@gmail.com",
    description="Module for handling JSON data in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pascal65536/utils",
    python_requires=">=3.10",
    package_dir={"utilspascal65536": "utilspascal65536"},
)
