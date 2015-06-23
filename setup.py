#!/usr/bin/env python
from setuptools import setup

setup(name="genome_coverage_plotter",
      version="0.1",
      description="Simple whole-genome coverage visualization.",
      author="Matt Edwards",
      author_email="matted@mit.edu",
      license="MIT",
      url="https://github.com/matted/genome_coverage_plotter",
      packages=[],
      scripts=["genome_coverage_plotter.py"],
      zip_safe=True,
      install_requires=["numpy", "pysam"],
     )
