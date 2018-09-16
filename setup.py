from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tf_metrics",
    version="0.0.1",
    author="Guillaume Genthial",
    description="Multi-class metrics for Tensorflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=find_packages(exclude=["test"]),
    package_data={'': ['*.json', '*.pl']},
    classifiers=(
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ),
    install_requires=[
        "numpy",
        "pytest",
        "tensorflow>=1.6"
    ]
)
