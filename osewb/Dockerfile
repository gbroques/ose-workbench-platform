FROM ubuntu:18.04

ARG USER=docker
ARG UID=1000
ARG GID=1000
ARG PASSWORD=docker

RUN useradd -m $USER --uid=$UID
RUN echo "$USER:$PASSWORD" | chpasswd

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    # software-properties-common for add-apt-repository command
    # Also installs Python 3 as a dependency which we use later
    software-properties-common \
    # Python 3 packages for pip install ose-workbench-platform
    python3-pip \
    python3-setuptools \
    python-wheel \
    # For sphinx.ext.graphviz and graphviz diagrams in docs
    graphviz

RUN python3 -m pip install --upgrade pip==20.1.1

# Install FreeCAD
RUN add-apt-repository ppa:freecad-maintainers/freecad-stable
RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    freecad

WORKDIR /var/app
COPY ./test-requirements.txt ./

# Install test dependencies with Python 2.7
RUN python3 -m pip install -r test-requirements.txt

# Install ose-workbench-platform for building docs inside container
# Typical docs/conf.py files import osewb.docs for standard base configuration
RUN python3 -m pip install ose-workbench-platform==0.1.0a19

# To give acess to FreeCAD in Python
ENV PYTHONPATH=/usr/lib/freecad/lib/

RUN ln -s /usr/lib/freecad/Mod /usr/lib/freecad-python3/Mod
RUN ln -s /usr/lib/freecad/Ext /usr/lib/freecad-python3/Ext

USER $UID:$GID

# Keep container running
CMD tail -f /dev/null
