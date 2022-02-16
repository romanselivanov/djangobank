FROM python:3.8 as django
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
RUN pip install poetry
RUN pip install setuptools==59.6.0
COPY backend/poetry.lock backend/pyproject.toml /backend/

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi
ADD backend/ /backend


FROM node:16 as nextjs

WORKDIR /app/
ADD nextjs/package.json /app/package.json
ADD nextjs/package-lock.json /app/package-lock.json
RUN npm ci
ADD nextjs /app/
RUN npm run build

EXPOSE 3000
