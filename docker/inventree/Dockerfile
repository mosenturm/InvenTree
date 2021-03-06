FROM python:alpine as production

# GitHub source
ARG repository="https://github.com/inventree/InvenTree.git"
ARG branch="master"

ENV PYTHONUNBUFFERED 1

# InvenTree key settings
ENV INVENTREE_HOME="/home/inventree"

# GitHub settings
ENV INVENTREE_REPO="${repository}"
ENV INVENTREE_BRANCH="${branch}"

ENV INVENTREE_LOG_LEVEL="INFO"

# InvenTree paths
ENV INVENTREE_SRC_DIR="${INVENTREE_HOME}/src"
ENV INVENTREE_MNG_DIR="${INVENTREE_SRC_DIR}/InvenTree"
ENV INVENTREE_DATA_DIR="${INVENTREE_HOME}/data"
ENV INVENTREE_STATIC_ROOT="${INVENTREE_HOME}/static"
ENV INVENTREE_MEDIA_ROOT="${INVENTREE_DATA_DIR}/media"
ENV INVENTREE_BACKUP_DIR="${INVENTREE_DATA_DIR}/backup"

ENV INVENTREE_CONFIG_FILE="${INVENTREE_DATA_DIR}/config.yaml"
ENV INVENTREE_SECRET_KEY_FILE="${INVENTREE_DATA_DIR}/secret_key.txt"

# Pass DB configuration through as environment variables
ENV INVENTREE_DB_ENGINE="${INVENTREE_DB_ENGINE}"
ENV INVENTREE_DB_NAME="${INVENTREE_DB_NAME}"
ENV INVENTREE_DB_HOST="${INVENTREE_DB_HOST}"
ENV INVENTREE_DB_PORT="${INVENTREE_DB_PORT}"
ENV INVENTREE_DB_USER="${INVENTREE_DB_USER}"
ENV INVENTREE_DB_PASSWORD="${INVENTREE_DB_PASSWORD}"

LABEL org.label-schema.schema-version="1.0" \
      org.label-schema.build-date=${DATE} \
      org.label-schema.vendor="inventree" \
      org.label-schema.name="inventree/inventree" \
      org.label-schema.url="https://hub.docker.com/r/inventree/inventree" \
      org.label-schema.version=${INVENTREE_VERSION} \
      org.label-schema.vcs-url=${INVENTREE_REPO} \
      org.label-schema.vcs-branch=${BRANCH} \
      org.label-schema.vcs-ref=${COMMIT}

# Create user account
RUN addgroup -S inventreegroup && adduser -S inventree -G inventreegroup
WORKDIR ${INVENTREE_HOME}

RUN mkdir ${INVENTREE_STATIC_ROOT}

# Install required system packages
RUN apk add --no-cache git make bash \
    gcc libgcc g++ libstdc++ \
    libjpeg-turbo libjpeg-turbo-dev jpeg jpeg-dev \
    libffi libffi-dev \
    zlib zlib-dev
RUN apk add --no-cache cairo cairo-dev pango pango-dev
RUN apk add --no-cache fontconfig ttf-droid ttf-liberation ttf-dejavu ttf-opensans ttf-ubuntu-font-family font-croscore font-noto
RUN apk add --no-cache python3
RUN apk add --no-cache postgresql-contrib postgresql-dev libpq
RUN apk add --no-cache mariadb-connector-c mariadb-dev

# Create required directories
#RUN mkdir ${INVENTREE_DATA_DIR}}/media ${INVENTREE_HOME}/static ${INVENTREE_HOME}/backup

# Install required python packages
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -U invoke
RUN pip install --no-cache-dir -U psycopg2 mysqlclient pgcli mariadb
RUN pip install --no-cache-dir -U gunicorn

# Clone source code
RUN echo "Downloading InvenTree from ${INVENTREE_REPO}"
RUN git clone --branch ${INVENTREE_BRANCH} --depth 1 ${INVENTREE_REPO} ${INVENTREE_SRC_DIR}

# Install InvenTree packages
RUN pip install --no-cache-dir -U -r ${INVENTREE_SRC_DIR}/requirements.txt

# Copy gunicorn config file
COPY gunicorn.conf.py ${INVENTREE_HOME}/gunicorn.conf.py

# Copy startup scripts
COPY start_server.sh ${INVENTREE_SRC_DIR}/start_server.sh
COPY start_worker.sh ${INVENTREE_SRC_DIR}/start_worker.sh

RUN chmod 755 ${INVENTREE_SRC_DIR}/start_server.sh
RUN chmod 755 ${INVENTREE_SRC_DIR}/start_worker.sh

# exec commands should be executed from the "src" directory
WORKDIR ${INVENTREE_SRC_DIR}

# Let us begin
CMD ["bash", "./start_server.sh"]
