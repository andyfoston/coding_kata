FROM python:3.7-alpine
WORKDIR /code
COPY . .
ENTRYPOINT ["python", "/code/basic_arithmetic.py"]