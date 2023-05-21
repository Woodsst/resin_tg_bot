FROM python:3.10

ARG APP_USER=appuser
ARG APP_USER_UID=1000
ARG APP_ROOT=/opt/app

ENV  PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_ROOT=${APP_ROOT}

RUN useradd --create-home --uid=${APP_USER_UID} ${APP_USER}

WORKDIR ${APP_ROOT}

RUN  apt-get update \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip --no-cache-dir \
    && chown ${APP_USER}:${APP_USER} ${APP_ROOT}

COPY requirements.txt ${APP_ROOT}requirements.txt

RUN pip install --no-cache-dir --upgrade -r ${APP_ROOT}requirements.txt

COPY --chown=${APP_USER}:${APP_USER} . .

USER ${APP_USER}:${APP_USER}

ENTRYPOINT ["python",  "main.py"]
