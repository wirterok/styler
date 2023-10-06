FROM python:3.10-slim-buster as base

ARG WORKDIR=/usr/src/app/

RUN apt-get update \
    && python -m pip install --upgrade pip  \
    && pip install poetry

WORKDIR /usr/src/build
COPY ./pyproject.toml ./poetry.lock /usr/src/build/
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

WORKDIR ${WORKDIR}
RUN useradd -m -d /home/app -N -G users -u 1313 app \
    && chown -R app:users ${WORKDIR} 
    # && chmod +x ${WORKDIR}

USER app
COPY . ${WORKDIR}

ENTRYPOINT ["./docker/start.sh"]