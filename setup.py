from setuptools import find_packages, setup

setup(
    name='kwiksand',
    packages=find_packages(include=['kwiksand']),
    version='1.1.0',
    description='a thing to write text character by character',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    install_requires=[],   
)
