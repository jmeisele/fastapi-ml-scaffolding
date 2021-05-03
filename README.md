# FastAPI Model Server Scaffolding

Serving machine learning models production-ready, fast, easy and secure powered by FastAPI by [Sebastián Ramírez](https://github.com/tiangolo).

This repository contains a starter app which can be used to speed-up your next machine learning project. 

To experiment and get a feeling on how to use this scaffolding, a sample regression model for house price prediction is included in this project. Follow the installation and setup instructions to run the sample model and serve it aso RESTful API.

## Requirements

Python 3.6+

## Installation/Setup
Makefile provided to get you up and going quickly.
```bash
make setup
```

## Run It
1. Start your  app with: 
```bash
poetry run uvicorn app.main:app
```

2. Go to [http://localhost:8000/docs](http://localhost:8000/docs).
   
3. You can use the sample payload from the `docs/sample_payload.json` file when trying out the house price prediction model using the API.
   ![Prediction with example payload](./docs/sample_payload.png)


## Testing
Makefile provided to provide test suite.
```bash
make test
```

## Linting & Formatting
Makefile provided to provide linting & formatting suite.
```bash
make format
```