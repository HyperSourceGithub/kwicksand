from setuptools import find_packages, setup

setup(
    name='kwiksand',
    packages=find_packages(include=['kwiksand']),
    version='0.1.4',
    description='a thing to write text character by character',
    author='HyperSource01',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown', 
    install_requires=[],   
)
