from setuptools import find_packages, setup

setup(
    name='archi',
    packages=find_packages(include=['archi']),
    version='1.0.0',
    description='Simple REST API wrapper for ved.archi',
    author='Blaze',
    license='MIT',
    install_requires=['requests'],
)