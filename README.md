genome_coverage_plotter 0.1
==============

[![Build Status](https://travis-ci.org/matted/census.svg?branch=master)](https://travis-ci.org/matted/genome_coverage_plotter) [![Coverage Status](https://coveralls.io/repos/matted/genome_coverage_plotter/badge.svg)](https://coveralls.io/r/matted/genome_coverage_plotter)

Installation:
==

*TODO.*

You can get genome_coverage_plotter by pulling it from git:

    git clone https://github.com/matted/genome_coverage_plotter.git

To run genome_coverage_plotter, several Python packages are required.  On a Ubuntu-like
system, these commands will get the appropriate dependencies:

    sudo apt-get install python python-dev build-essential python-setuptools python-numpy python-scipy python-pylab
    sudo easy_install pysam

If you don't have root permissions on your system, but you already
have Python, setuptools, gcc, Scipy, and Numpy, you can get Census
working by cloning it, moving into the new directory, and running:

    python setup.py install --user

This will install the pysam dependency in your local user directory.
The Scipy and Numpy dependencies are best installed at the system
level since they require several non-Python components.

If you want the Census tools on your system path (and want to get the
pysam dependency automatically), install Census with:

    sudo python setup.py install

There is also a Docker image that has genome_coverage_plotter and its dependencies
preinstalled.  

Quick usage:
==

*TODO.*

![example](https://raw.githubusercontent.com/matted/genome_coverage_plotter/master/yeast_test.bam.depth.png)
