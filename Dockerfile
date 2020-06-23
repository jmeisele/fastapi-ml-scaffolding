FROM python:3.7-stretch
RUN pip install pipenv
COPY Pipfile* /tmp
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/myapp
RUN pip install /tmp/myapp
CMD ["uvicorn", "fastapi_scaffolding.main:app", "host='0.0.0.0'", "port=3000"]