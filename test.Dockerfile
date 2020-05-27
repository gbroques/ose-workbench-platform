FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    # software-properties-common for add-apt-repository command
    software-properties-common \
    # Python 2.7 packages for pip install -r requirements.txt
    python-pip \
    python-setuptools \
    python-wheel

RUN pip install --upgrade pip==20.1.1

# Install FreeCAD
RUN add-apt-repository ppa:freecad-maintainers/freecad-legacy
RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    freecad-0.16

WORKDIR /var/app
COPY ./test-requirements.txt ./

# For generate_property_tables script
COPY ./bin /usr/bin/
RUN chmod +x /usr/bin/generate_property_tables.py

# Install test dependencies
RUN pip install -r test-requirements.txt

# To give acess to FreeCAD in Python
ENV PYTHONPATH=/usr/lib/freecad-0.16/lib/

# Keep container running
CMD tail -f /dev/null
