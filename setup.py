import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
  name='ztag',
  version='1.0.0',
  description='utility for transforming and annotating JSON scan data with additional metdata',
  licsense="Apache License, Version 2.0",
  long_description=open(os.path.join(here, 'README.md')).read(),
  classifiers=[
    "Programming Language :: Python",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English"
  ],
  author='ZMap Team',
  author_email='zmap-team@umich.edu',
  url='https://github.com/zmap/ztag',
  keywords='zmap censys ztag internet-wide scanning',
  packages=find_packages(),
  include_package_data=True,
  zip_safe=False,
  install_requires = [
    "redis",
    "protobuf==3.0.0a3",
    "python-dateutil",
    "zsearch_definitions"
  ],
  entry_points = {
    'console_scripts': [
      'ztag = ztag.__main__:main',
    ]
  }
)

