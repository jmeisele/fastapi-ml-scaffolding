FROM python:3.6.13 as base

# copy our project code
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
# install our dependencies
RUN pip3 install -r requirements.txt

COPY . /app

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "app.main:app"]