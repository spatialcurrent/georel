#!/usr/bin/env python


from setuptools import setup

setup(
    name='georel',
    version='1.0.0',
    install_requires=[],
    author='Spatial Current Developers',
    author_email='opensource@spatialcurrent.io',
    license='BSD License',
    url='https://github.com/spatialcurrent/georel/',
    keywords='python',
    description='A Python library for parsing geospatial relationships from natural language.',
    long_description=open('README.rst').read(),
    download_url="https://github.com/spatialcurrent/georel/zipball/master",
    packages=["georel"],
    package_data={'': ['LICENSE', 'NOTICE'], 'georel': ['*.pem']},
    package_dir={'georel': 'georel'},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
