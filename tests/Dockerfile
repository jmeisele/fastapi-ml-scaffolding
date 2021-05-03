FROM python:3.6.13 as base

# copy our project code
COPY ./requirements-dev.txt /app/requirements-dev.txt

WORKDIR /app

# install our dependencies
RUN pip3 install -r requirements-dev.txt

COPY . /app

# expose the port 8000
EXPOSE 8000

# run unit tests and get coverage report
CMD ["python", "-m", "pytest"]