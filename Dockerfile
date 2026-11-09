FROM python:3.14-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root \
    && pip install --no-cache-dir gunicorn

COPY . .

EXPOSE 10000

CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn bookstore.wsgi:application --bind 0.0.0.0:${PORT:-10000}"]
