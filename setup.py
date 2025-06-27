DESCRIPTION = """
Copyright (C) 2020-2025 Sergey V. Pakhtusov aka pascal65536

This Python project to be a versatile utility library offering a wide range of functionalities, including.

Working with matrices. Matrix transformation of 2D space.
"""


from setuptools import find_namespace_packages, setup, find_packages


setup(
    name="behoof",
    version="1.2.0",
    packages=find_packages(),
    install_requires=[],
    author="Sergey V. Pakhtusov",
    author_email="pascal65536@gmail.com",
    description="A general-purpose utility library offering a wide range of functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pascal65536/behoof",
    python_requires=">=3.10",
    package_dir={"behoof": "behoof"},
)
