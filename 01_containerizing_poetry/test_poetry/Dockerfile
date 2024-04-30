FROM python:alpine3.18

COPY . /app

WORKDIR /app

RUN pip install poetry \
&& poetry config virtualenvs.create false\
&& poetry install

CMD ["poetry", "run", "uvicorn", "test_poetry.main:app","--host","0.0.0.0","--port","8000"]
