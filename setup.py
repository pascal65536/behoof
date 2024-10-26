DESCRIPTION = """
Copyright (C) 2020-2024 Sergey V. Pakhtusov (pascal65536@gmail.com)
Module for handling JSON data in Python.
"""


from setuptools import setup, find_packages

setup(
    name="pascal65536_utils",
    version="1.0.6",
    packages=find_packages(),
    install_requires=[],
    author="Sergey V. Pakhtusov",
    author_email="pascal65536@gmail.com",
    description="Module for handling JSON data in Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pascal65536/utils",
)


# setupOpts = dict(
#     name="pascal65536_utils",
#     description="Module for handling JSON data in Python",
#     long_description=DESCRIPTION,
#     license="MIT",
#     url="https://kompoblog.ru/",
#     project_urls={
#         "Documentation": "https://kompoblog.ru",
#         "Source": "https://github.com/pascal65536/utils",
#     },
#     author="Sergey V. Pakhtusov",
#     author_email="pascal65536@gmail.com",
#     classifiers=[
#         "Programming Language :: Python",
#         "Programming Language :: Python :: 3",
#         "Development Status :: 2 - Beta",
#         "Environment :: Other Environment",
#         "Intended Audience :: Science/Research",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#         "Topic :: Software Development :: Libraries :: Python Modules",
#         "Topic :: Scientific/Engineering :: JSON data",
#         "Topic :: Software Development :: Handling JSON data",
#     ],
# )


# from setuptools import find_namespace_packages, setup


# setup(
#     version="1.0.5",
#     packages=find_namespace_packages(
#         include=["pascal65536_utils", "pascal65536_utils.*"]
#     ),
#     python_requires=">=3.8",
#     package_dir={"pascal65536_utils": "pascal65536_utils"},
#     install_requires = [
#     ],
#     **setupOpts,
# )
