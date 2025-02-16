"""
App for serving TensorFlow models on Cloud Foundry/IBM Cloud.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ibm-visual-recognition',
    version='1.0.0',
    description='Web App for serving a pretrained TensorFlow model in production using IBM Watson machine learning.',
    long_description=long_description,
    license='Apache-2.0'
)
