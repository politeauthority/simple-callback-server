FROM debian:jessie
RUN apt-get update
RUN apt-get install -y --no-install-recommends --fix-missing \
    python-pip \
    python \
    wget \
    unzip \
    python-mysqldb

RUN mkdir /data/ && \
    cd /opt/ && \
    wget https://github.com/politeauthority/simple-callback-server/archive/master.zip && \
    unzip master.zip &&\
    mv simple-callback-server-master simple-callback-server &&\
    cd simple-callback-server && \
    pip install -r requirements.txt

ENV SCS_MYSQL_HOST="Host"
ENV SCS_MYSQL_USER="User"
ENV SCS_MYSQL_PASS="Pass"
ENV SCS_MYSQL_PORT=3306
ENV SCS_MYSQL_NAME="stocky"
ENV SCS_BASE_LOGGING_DIR='/data/logs'
ENV SCS_ADMIN_URL="the-admin"
ENV SCS_BUILD="LIVE"

ENV SCS_APP_DATA_PATH="/data/"
ENV TZ=America/Denver

VOLUME /opt/simple-callback-server/
VOLUME /data/

EXPOSE 80

CMD python /opt/simple-callback-server/run.py
