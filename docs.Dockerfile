FROM python:3.8.1-alpine3.11

# Install make with Alpine Linux package manager
RUN apk add make

WORKDIR /var/app
COPY ./docs-requirements.txt ./

RUN pip install -r docs-requirements.txt

# Keep container running
CMD tail -f /dev/null
