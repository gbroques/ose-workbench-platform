FROM ubuntu:16.04

RUN apt-get update

# For add-apt-repository command
RUN apt-get install -y software-properties-common

# Install FreeCAD
RUN add-apt-repository ppa:freecad-maintainers/freecad-legacy
RUN apt-get update
RUN apt-get install -y freecad-0.16

# Install pip
RUN apt-get install -y python-pip --fix-missing
RUN pip install --upgrade pip

ENV PYTHONPATH=/usr/lib/freecad-0.16/lib/

WORKDIR /var/app
COPY ./test-requirements.txt ./
COPY ./bin /usr/bin/
RUN chmod +x /usr/bin/generate_property_tables.py

# Install test dependencies
RUN pip install -r test-requirements.txt

# Keep container running
CMD tail -f /dev/null
