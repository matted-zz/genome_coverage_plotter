FROM ipython/scipystack

MAINTAINER Matt Edwards <matted@mit.edu>

RUN mkdir /root/genome_coverage_plotter
WORKDIR /root/genome_coverage_plotter
RUN git clone https://github.com/matted/genome_coverage_plotter.git .

RUN curl -o miniconda.sh http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
RUN chmod a+x miniconda.sh
RUN ./miniconda.sh -b
RUN /root/miniconda/bin/conda update --yes conda
RUN /root/miniconda/bin/conda create --yes -n conda python=2.7
RUN /root/miniconda/bin/conda install --yes python=2.7 numpy pysam matplotlib seaborn pandas

ENV PATH /root/miniconda/bin/:$PATH

# RUN python setup.py install --quiet

CMD echo "Please run plot_coverage.py."

# Examples:
#
# Build the image:
# docker build -t=matted/genome_coverage_plotter .
#
# Investigate the image:
# docker run -t --rm=true -i matted/genome_coverage_plotter /bin/bash
#
