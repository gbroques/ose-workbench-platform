FROM python:3.8.1-alpine3.11

WORKDIR /var/app

RUN pip install ose-workbench-platform==0.1.0a8

# Keep container running
CMD tail -f /dev/null
