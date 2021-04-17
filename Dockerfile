FROM python:3.9-slim-buster

ENV VIRTUAL_ENV=/opt/venv
ENV PYTHONBUFFERED 1

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/code/


EXPOSE 8000

WORKDIR /tmp/code/src/

CMD gunicorn --workers 3 --bind 0.0.0.0:8000 {{project_name}}.wsgi:application